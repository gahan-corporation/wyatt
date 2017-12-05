# Part of Odoo. See LICENSE file for full copyright and licensing details.

import gerp.tests


@gerp.tests.common.at_install(False)
@gerp.tests.common.post_install(True)
class TestUi(gerp.tests.HttpCase):
    def test_admin(self):
        self.phantom_js("/", "gerp.__DEBUG__.services['web_tour.tour'].run('blog')", "gerp.__DEBUG__.services['web_tour.tour'].tours.blog.ready", login='admin')
