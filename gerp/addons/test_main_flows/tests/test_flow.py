# Part of Gerp. See LICENSE file for full copyright and licensing details.

import gerp.tests


@gerp.tests.common.at_install(False)
@gerp.tests.common.post_install(True)
class TestUi(gerp.tests.HttpCase):
    
    def test_01_main_flow_tour(self):
        self.phantom_js("/web", "gerp.__DEBUG__.services['web_tour.tour'].run('main_flow_tour')", "gerp.__DEBUG__.services['web_tour.tour'].tours.main_flow_tour.ready", login="admin", timeout=180)
