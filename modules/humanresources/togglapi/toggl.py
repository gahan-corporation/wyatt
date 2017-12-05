"""Get time entries from Toggl."""
import requests
import yaml


class Toggl(object):
    """Class for getting and processing Toggl entries."""
    config = {}
    entries = {}
    token = ''
    user = {}

    def __init__(self, **auth):
        config_file = open('.toggl.yml', 'r')
        config = yaml.load(config_file.read())
        config_file.close()
        user = config.get('users', auth.get('user'))
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
