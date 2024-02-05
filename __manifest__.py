# -*- coding: utf-8 -*-
{
    'name': "School Subject",

    'summary': """
        Manage school subject data""",

    'description': """
        Manage school subject data in Odoo with this module.
    """,

    'author': "Gabriel Humerez Romero",
    'website': "https://www.linkedin.com/in/gabrielhumerez",

    'sequence': -100,
    'category': 'School Management',
    'version': '1.0',

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/subjects_view.xml',
        'views/students_view.xml',
        'views/teachers_view.xml',
        'views/menu_view.xml',
    ],

    'application': True,
    'installable': True,
    'auto_install': False,
}
