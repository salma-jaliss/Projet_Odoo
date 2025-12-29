{
    'name': 'Gestion des Tâches en Tableau',
    'version': '1.0',
    'summary': 'Module pour gérer les tâches en tableau Kanban',
    'description': 'Ce module permet de créer des tableaux de tâches avec vue Kanban pour une gestion collaborative.',
    'author': 'ASO',
    'license': 'LGPL-3',
    'category': 'Productivity',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/board_views.xml',
        'views/task_views.xml',
    ],
    'installable': True,
    'application': True,
}
