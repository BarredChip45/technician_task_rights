# -*- coding: utf-8 -*-
from odoo import models, api


class IrUiMenu(models.Model):
    _inherit = 'ir.ui.menu'

    @api.model
    def search(self, domain, offset=0, limit=None, order=None):
        """
        Override search to filter menus for technicians.
        """
        # Check if current user is a technician (not a manager)
        user = self.env.user
        is_technician = user.has_group('technician_task_mgmt.group_technician')
        is_manager = user.has_group('technician_task_mgmt.group_tech_manager')

        # Only filter for technicians who are NOT managers
        if is_technician and not is_manager:
            try:
                # Get the Max Techniciens menu
                tech_menu = self.env.ref('technician_task_mgmt.menu_tt_root', raise_if_not_found=False)
                if tech_menu:
                    # Get all children recursively using SQL
                    self.env.cr.execute("""
                        WITH RECURSIVE menu_tree AS (
                            SELECT id, parent_id FROM ir_ui_menu WHERE id = %s
                            UNION ALL
                            SELECT m.id, m.parent_id FROM ir_ui_menu m
                            INNER JOIN menu_tree mt ON m.parent_id = mt.id
                        )
                        SELECT id FROM menu_tree
                    """, (tech_menu.id,))

                    allowed_ids = [row[0] for row in self.env.cr.fetchall()]

                    # Add domain to restrict to allowed menu IDs
                    domain = domain + [('id', 'in', allowed_ids)]
            except Exception:
                pass

        return super().search(domain, offset=offset, limit=limit, order=order)
