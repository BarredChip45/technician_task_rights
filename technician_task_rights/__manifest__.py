{
    'name': 'Technician Task Rights',
    'version': '18.0.1.0.0',
    'category': 'Technician Max',
    'summary': 'Restrict technicians from changing kanban stages manually',
    'description': """
        This module prevents technicians from manually changing the kanban stages of tasks.
        Only managers with the 'Technician Task Manager' group can modify task stages manually.
        Technicians can still use the start/stop buttons which automatically change stages.
    """,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'depends': ['technician_task_mgmt'],
    'data': [],
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'LGPL-3',
}