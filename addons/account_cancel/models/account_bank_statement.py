# -*- coding: utf-8 -*-
# Part of Gerp. See LICENSE file for full copyright and licensing details.

from gerp import models, api, _
from gerp.exceptions import UserError


class BankStatement(models.Model):
    _inherit = 'account.bank.statement'

    @api.multi
    def button_draft(self):
        self.state = 'open'


