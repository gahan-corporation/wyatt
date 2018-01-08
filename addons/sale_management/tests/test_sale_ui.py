import gerp.tests
# Part of Gerp. See LICENSE file for full copyright and licensing details.

@gerp.tests.common.at_install(False)
@gerp.tests.common.post_install(True)
class TestUi(gerp.tests.HttpCase):

    def test_01_sale_tour(self):
        self.phantom_js("/web", "gerp.__DEBUG__.services['web_tour.tour'].run('sale_tour')", "gerp.__DEBUG__.services['web_tour.tour'].tours.sale_tour.ready", login="admin")
