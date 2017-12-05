# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import gerp.tests


@gerp.tests.common.at_install(False)
@gerp.tests.common.post_install(True)
class TestUi(gerp.tests.HttpCase):
    def test_01_admin_shop_tour(self):
        self.phantom_js("/", "gerp.__DEBUG__.services['web_tour.tour'].run('shop')", "gerp.__DEBUG__.services['web_tour.tour'].tours.shop.ready", login="admin")

    def test_02_admin_checkout(self):
        self.phantom_js("/", "gerp.__DEBUG__.services['web_tour.tour'].run('shop_buy_product')", "gerp.__DEBUG__.services['web_tour.tour'].tours.shop_buy_product.ready", login="admin")

    def test_03_demo_checkout(self):
        self.phantom_js("/", "gerp.__DEBUG__.services['web_tour.tour'].run('shop_buy_product')", "gerp.__DEBUG__.services['web_tour.tour'].tours.shop_buy_product.ready", login="demo")

    # TO DO - add public test with new address when convert to web.tour format.
