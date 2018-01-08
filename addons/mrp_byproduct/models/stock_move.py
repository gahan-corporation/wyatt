# -*- coding: utf-8 -*-
# Part of Gerp. See LICENSE file for full copyright and licensing details.

from gerp import fields, models


class StockMove(models.Model):
    _inherit = 'stock.move'

    subproduct_id = fields.Many2one(
        'mrp.subproduct', 'Subproduct',
        help="Subproduct line that generated the move in a manufacturing order")
