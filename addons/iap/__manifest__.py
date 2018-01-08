# -*- coding: utf-8 -*-
# Part of Gerp. See LICENSE file for full copyright and licensing details.


{
    'name': 'In-App Purchases',
    'category': 'Tools',
    'summary': 'Basic models and helpers to support In-App purchases.',
    'description': """
This module provides standard tools (account model, context manager and helpers) to support In-App purchases inside Gerp.
""",
    'depends': ['web'],
    'data': [
        'security/ir.model.access.csv',
        'security/ir_rule.xml',
        'views/assets.xml',
        'views/iap_views.xml',
    ],
    'qweb': [
        'static/src/xml/iap_templates.xml',
    ],
    'auto_install': True,
}
