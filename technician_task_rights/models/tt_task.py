from odoo import models, api, exceptions, _


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