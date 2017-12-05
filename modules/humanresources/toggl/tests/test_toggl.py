"""Module for testting Toggl integration."""
import toggl.toggl as tgl

class TestToggl(object):
    """TestToggl class."""
    toggl = {}

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

    def test_get_project(self):
        """Test if the correct Toggl project is returend"""
        assert self.token is True

    def test_get_entry(self):
        """Get a time entry."""
        assert self.token is True

    def test_model_fields(self):
        """Ensure that the database model has all the right fields."""
        assert self.token is True

    def test_get_workspaces_by_status(self):
        """Make sure we're getting the correct worksapces."""
        local_toggl = tgl.Toggl(user='xander_dp')
        self.workspaces = local_toggl.get_workspaces()
        assert self.workspaces.status_code == 200

    def test_workspaces_write_results(self):
        """Make sure we can read results we got from the api."""
        workspaces_raw = self.toggl.load_workspaces()
        print(type(workspaces_raw))
