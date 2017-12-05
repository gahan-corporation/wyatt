"""Get time entries from Toggl."""
import configparser
import requests


class Toggl(object):
    """Class for getting and processing Toggl entries."""
    config = configparser.ConfigParser()
    entries = {}
    token = ''
    user = {}

    def __init__(self, **auth):
        self.config.read('.toggl_tokens')
        user = self.config.get('users', auth.get('user'))
        self.token = user.get('token')

    def get_user(self):
        """Get the user who we're interested in."""
        self.user = requests.get(
            self.config.get('toggl', 'me'),
            requests.auth.HTTPBasicAuth(self.token, 'api_token'))
        print(self.user)
        return self.user

    def get_current_timer(self):
        """Check for a running timer."""
        return self.entries

    def get_active_projects(self):
        """Add active projects."""
        return self.user
