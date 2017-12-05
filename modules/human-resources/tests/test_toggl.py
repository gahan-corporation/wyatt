"""Module for testting Toggl integration."""
import configparser


class TestToggl(object):
    """TestToggl class."""
    conf = configparser.ConfigParser()
    token = None

    def test_valid_config(self):
        """Make sure that there are valid tokens proviided."""
        tokens = self.conf.read('.toggl_tokens')
        print(tokens)
        assert tokens is False

    def test_api_token(self):
        """Ensure the api token works."""
        assert self.token is True

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
