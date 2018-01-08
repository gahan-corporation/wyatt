# -*- coding: utf-8 -*-
# Part of Gerp. See LICENSE file for full copyright and licensing details.

from gerp import api, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    @api.onchange('can_be_expensed')
    def _onchange_can_be_expensed(self):
        if not self.can_be_expensed:
            self.expense_policy = 'no'
