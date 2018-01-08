# -*- coding: utf-8 -*-
# Part of Gerp. See LICENSE file for full copyright and licensing details.

{
    'name': "Calendar SMS",
    'summary': 'Send text messages as event reminders',
    'description': "Send text messages as event reminders",
    'category': 'Hidden',
    'version': '1.0',
    'depends': ['calendar', 'sms'],
    'data': [
        'views/calendar_views.xml',
    ],
    'application': False,
    'auto_install': True,
}
