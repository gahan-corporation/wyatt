"""Module for testting Toggl integration."""


class TestToggl(object):
    """TestToggl class."""
    token = None

    def test_api_token(self):
        """Ensure the api token works."""
        assert self.token is True

    def test_get_entry(self):
        """Get a time entry."""
        assert self.token is True
