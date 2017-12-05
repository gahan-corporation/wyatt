"""Module for testting Toggl integration."""
import json

import toggl.toggl as tgl


class TestToggl(object):
    """TestToggl class."""
    projects = {}
    toggl = {}
    token = ''
    workspaces = {}
    ws_json = {}

    def test_get_user_auth(self):
        """Test that we can get the correct user from the api."""
        self.toggl = tgl.Toggl(user='xander_dp')
        user = self.toggl.get_user()
        assert user.status_code == 200

    def test_get_user_fail(self):
        """Test that incorrect auth produces a 403."""
        self.toggl = tgl.Toggl(user='nouser')
        user = self.toggl.get_user()
        assert user.status_code == 403

    def test_get_active_project(self):
        """Test if the correct Toggl project is returend"""
        local_toggl = tgl.Toggl(user='xander_dp')
        self.projects = local_toggl.get_active_projects()
        assert isinstance(self.projects, list)

        for item in self.projects:
            assert isinstance(item, dict)

    def test_get_token(self):
        """Get a time entry."""
        local_toggl = tgl.Toggl(user='xander_dp')
        self.token = local_toggl.get_token()
        assert len(self.token) == 32

    def test_get_workspaces_by_status(self):
        """Make sure we're getting the correct worksapces."""
        local_toggl = tgl.Toggl(user='xander_dp')
        self.workspaces = local_toggl.get_workspaces()
        assert self.workspaces.status_code == 200

    def test_workspaces_write_results(self):
        """Make sure we can read results we got from the api."""
        ws_file = open('.workspaces.json', 'r')
        ws_string = ws_file.read()
        ws_file.close()
        ws_dict = json.loads(ws_string)
        with open('.workspaces.json', 'r') as ws_file:
            self.ws_json = json.load(ws_file)
        assert self.ws_json == ws_dict
