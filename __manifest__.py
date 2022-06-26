# -*- coding: utf-8 -*-
{
    'name': "Material Keda Tech",

    'summary': """
        Register material Keda Tech""",

    'description': """
    """,

    'author': "Keda Tech",
    'website': "https://www.keda-tech.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Material',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': True,
}