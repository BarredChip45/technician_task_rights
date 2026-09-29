from datetime import datetime, time, timedelta

import pytz

from odoo import models, api, exceptions, fields, _
from odoo.osv import expression


class TTTask(models.Model):
    _inherit = "tt.task"

    def write(self, vals):
        # Empêcher changement d'étape manuel si pas manager
        if 'stage_id' in vals and not self.env.user.has_group('technician_task_mgmt.group_tech_manager'):
            # Vérifier si c'est un changement manuel direct (pas de changement de state en même temps)
            # et pas via un contexte de synchronisation
            if not ('state' in vals or self.env.context.get('_skip_stage_sync')):
                raise exceptions.AccessError(_("Vous n'avez pas le droit de changer l'étape Kanban manuellement."))
        return super().write(vals)

    @api.model
    def _search(self, domain, *args, **kwargs):
        """Technicians only see tasks scheduled up to the end of today (their
        timezone); future tasks are hidden. Managers/other users are unaffected.
        Applied in _search so it also covers kanban, list and m2o dropdowns."""
        domain = self._tt_apply_technician_date_filter(domain)
        return super()._search(domain, *args, **kwargs)

    def _tt_apply_technician_date_filter(self, domain):
        user = self.env.user
        if (self.env.su
                or self.env.context.get('tt_bypass_date_filter')
                or user.has_group('technician_task_mgmt.group_tech_manager')
                or not user.has_group('technician_task_mgmt.group_technician')):
            return domain
        # Boundary = tomorrow midnight in the user's timezone, expressed as the
        # naive UTC value stored in the DB. A task at 30/09 00:00 local is thus
        # hidden on 29/09, while 29/09 23:59 and earlier stay visible.
        # tz.localize() on the naive local midnight applies the correct offset
        # for that wall-clock time, so DST (summer/winter) transitions are safe.
        tz = pytz.timezone(user.tz or 'UTC')
        today_local = pytz.utc.localize(fields.Datetime.now()).astimezone(tz).date()
        tomorrow_midnight_naive = datetime.combine(today_local + timedelta(days=1), time.min)
        boundary = tz.localize(tomorrow_midnight_naive).astimezone(pytz.utc).replace(tzinfo=None)
        date_domain = ['|', ('scheduled_date', '=', False), ('scheduled_date', '<', boundary)]
        return expression.AND([domain or [], date_domain])
