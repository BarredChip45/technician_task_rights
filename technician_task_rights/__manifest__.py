{
    'name': 'Technician Task Rights',
    'version': '18.0.1.0.0',
    'category': 'Technician Max',
    'summary': 'Restrict technicians access to only Max Techniciens app',
    'description': """
        This module restricts technicians to see only the Max Techniciens application.

        Features:
        - Technicians can only access Max Techniciens app
        - Managers can access all applications
        - Automatically hides all other apps for technicians
        - Prevents technicians from manually changing kanban stages of tasks
        - Technicians can still use the start/stop buttons which automatically change stages
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