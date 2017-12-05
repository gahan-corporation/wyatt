"""Module for testting Toggl integration."""
import toggl.api as toggl


class TestToggl(object):
    """TestToggl class."""
    toggl = {}

    def test_get_user(self):
        """Make sure that there are valid tokens proviided."""
        self.toggl = toggl.Toggl(user='xander.dpone')

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
