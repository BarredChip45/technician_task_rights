{
    'name': 'Technician Task Rights',
    'version': '18.0.1.1.0',
    'category': 'Technician Max',
    'summary': 'Technician access restrictions: kanban stages, card ordering and date visibility',
    'description': """
        This module tightens what technicians can do on technician tasks. Managers
        (group 'Technician Task Manager') keep full control.

        Restrictions applied to technicians:

        - Kanban stages: technicians cannot change a task's kanban stage manually
          (drag & drop between columns). Stages only move through the start/finish
          buttons, which change them automatically.

        - Kanban ordering: every user can reorder the cards by drag & drop EXCEPT
          technicians. The chosen order (task 'sequence') is shared and shown
          identically to technicians, who cannot change it. Enforced both in the
          UI (kanban is not draggable for technicians) and server-side.

        - Date visibility: technicians only see their own tasks scheduled up to the
          end of the current day in their timezone. Future tasks (tomorrow and
          later) are hidden until their day arrives; past and same-day tasks stay
          visible. Managers are not affected.
    """,
    'author': 'Kenan Globalis',
    'website': 'https://www.yourcompany.com',
    'depends': ['technician_task_mgmt'],
    'data': [],
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'LGPL-3',
}