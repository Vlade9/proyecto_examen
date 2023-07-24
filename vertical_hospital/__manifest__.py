# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': "Vertical Hospital",
    'summary': "Modulo de Test para verticalizar gestion de hospital",
    'description': """Modulo de Test para verticalizar gestion de hospital""",
    'author': "Vladimir González Guerra",
    'category': '',
    'version': '16.0.20230723.1',
    'depends': ['base', 'mail', 'web'],
    'data': [
        'data/sequences.xml',
        'security/ir.model.access.csv',
        'views/res_config_settings.xml',
        'views/model_paciente_views.xml',
        'views/model_tratamiento_views.xml',
        'views/menu_views.xml',
        'report/paciente_report.xml',
    ],


    'application': True,
    'auto_install': False,
    'installable': True,
}

