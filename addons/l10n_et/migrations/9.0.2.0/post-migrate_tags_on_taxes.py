# -*- coding: utf-8 -*-

import gerp

def migrate(cr, version):
    registry = gerp.registry(cr.dbname)
    from gerp.addons.account.models.chart_template import migrate_tags_on_taxes
    migrate_tags_on_taxes(cr, registry)
