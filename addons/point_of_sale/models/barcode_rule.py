# -*- coding: utf-8 -*-
# Part of Gerp. See LICENSE file for full copyright and licensing details.

from gerp import models, fields
from gerp.tools.translate import _


class BarcodeRule(models.Model):
    _inherit = 'barcode.rule'

    type = fields.Selection(selection_add=[
            ('weight', _('Weighted Product')),
            ('price', _('Priced Product')),
            ('discount', _('Discounted Product')),
            ('client', _('Client')),
            ('cashier', _('Cashier'))
        ])
