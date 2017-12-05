"""Module for testting Toggl integration."""
import configparser
import requests

import humanresources.toggle.api


class TestToggl(object):
    """TestToggl class."""
    conf = configparser.ConfigParser()
    headers = {
        'Content-Type': 'application/json'
    }
    toggl_api_me = 'https://www.toggl.com/api/v8/me'
    token = ()

    def test_valid_config(self):
        """Make sure that there are valid tokens proviided."""
        self.conf.read('.toggl_tokens')
        token = self.conf.get('xander.dpone', 'token')
        user = requests.get(
            self.toggl_api_me,
            auth=requests.auth.HTTPBasicAuth(token, 'api_token'))
        print(user)
        print(len(token))
        print(type(token))
        assert self.conf.sections() is False

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
