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
        """Load relevant configs."""
        config_file = open('.toggl.yml', 'r')
        self.config = yaml.load(config_file.read())
        config_file.close()

        user = self.config.get('users').get(auth.get('user'))
        self.token = user.get('token')

    def get_user(self):
        """Get the user who we're interested in."""
        print(self.token)
        print(self.config.get('toggl').get('me'))
        self.user = requests.get(
            url=self.config.get('toggl').get('me'),
            auth=(self.token, 'api_token')
        )
        print(self.user.__dict__)
        return self.user

    def get_current_timer(self):
        """Check for a running timer."""
        return self.entries

    def get_active_projects(self):
        """Add active projects."""
        return self.user
