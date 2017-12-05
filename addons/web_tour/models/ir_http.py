# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from gerp import models
from gerp.http import request


class Http(models.AbstractModel):
    _inherit = 'ir.http'

    def session_info(self):
        result = super(Http, self).session_info()
        if result['is_superuser']:
            result['web_tours'] = request.env['web_tour.tour'].get_consumed_tours()
        return result
