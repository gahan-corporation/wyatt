"""Module for testting Toggl integration."""
import toggl.toggl as tgl

class TestToggl(object):
    """TestToggl class."""
    toggl = {}

    def test_get_user_auth(self):
        """Test that we can get the correct user from the api."""
        self.toggl = tgl.Toggl(user='xander_dp')
        user = self.toggl.get_user()
        print(user)

    def test_get_user_fail(self):
        """Test that incorrect auth produces a 403."""
        self.toggl = tgl.Toggl(user='nouser')
        user = self.toggl.get_user()
        print(user)

    def test_get_project(self):
        """Test if the correct Toggl project is returend"""
        assert self.token is True

    def test_get_entry(self):
        """Get a time entry."""
        assert self.token is True

    def test_model_fields(self):
        """Ensure that the database model has all the right fields."""
        assert self.token is True

    def test_triggering_events(self):
        """Test ability to respond to triggering events."""
        assert self.token is True
