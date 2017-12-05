# -*- coding: utf-8 -*-

import gerp

def migrate(cr, version):
    registry = gerp.registry(cr.dbname)
    from gerp.addons.account.models.chart_template import migrate_set_tags_and_taxes_updatable
    migrate_set_tags_and_taxes_updatable(cr, registry, 'l10n_de_skr04')
