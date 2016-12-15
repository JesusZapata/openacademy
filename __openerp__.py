# -*- coding: utf-8 -*-
{
    'name': "Open Academy",

    'summary': """Manage trainings""",

    'author': "Jesus Zapata",
    'website': "http://www.vauxoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'view/openacademy_course_view.xml',
        'view/openacademy_session_view.xml',
        'view/partner_view.xml',
        'view/session_workflow.xml',
        'view/openacademy_wizard.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/openacademy_course_demo.xml',
    ],
    'installable': True,
    'auto_install': False,
}
