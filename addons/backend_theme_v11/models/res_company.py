# -*- coding: utf-8 -*-
# Copyright 2016, 2017 Openworx
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from gerp import models, fields

class ResCompany(models.Model):

    _inherit = 'res.company'

    dashboard_background = fields.Binary(attachment=True)