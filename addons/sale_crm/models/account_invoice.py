# -*- coding: utf-8 -*-
# Part of Gerp. See LICENSE file for full copyright and licensing details.

from gerp import models


class AccountInvoice(models.Model):
    _name = "account.invoice"
    _inherit = ['account.invoice', 'utm.mixin']
