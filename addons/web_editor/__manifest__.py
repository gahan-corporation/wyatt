# -*- coding: utf-8 -*-
# Part of Gerp. See LICENSE file for full copyright and licensing details.

{
    'name': 'Web Editor',
    'category': 'Hidden',
    'description': """
Gerp Web Editor widget.
==========================

""",
    'depends': ['web'],
    'data': [
        'security/ir.model.access.csv',
        'views/editor.xml',
        'views/iframe.xml',
        'views/snippets.xml',
    ],
    'qweb': [
        'static/src/xml/*.xml',
    ],
    'auto_install': True
}
