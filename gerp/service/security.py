# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import gerp
import gerp.exceptions

def login(db, login, password):
    res_users = gerp.registry(db)['res.users']
    return res_users._login(db, login, password)

def check(db, uid, passwd):
    res_users = gerp.registry(db)['res.users']
    return res_users.check(db, uid, passwd)
