"""Get time entries from Toggl."""
import json
import requests
import yaml


class Toggl(object):
    """Class for getting and processing Toggl entries."""
    config = {}
    entries = {}
    projects = {}
    token = ''
    user = {}
    workspaces = {}

    def __init__(self, **auth):
        """Load relevant configs."""
        config_file = open('.toggl.yml', 'r')
        self.config = yaml.load(config_file.read())
        config_file.close()

        user = self.config.get('users').get(auth.get('user'))
        self.token = user.get('token')

    def get_user(self):
        """Get the user who we're interested in."""
        self.user = requests.get(
            url=self.config.get('toggl').get('me'),
            auth=(self.token, 'api_token')
        )
        return self.user

    def get_token(self):
        """Returns the value of the current token."""
        return self.token

    # def get_current_timer(self):
    #     """Check for a running timer."""
    #     return self.entries

    def get_active_projects(self):
        """Add active projects."""
        if not self.workspaces:
            workspaces = self.get_workspaces()
            ws_id = workspaces.json()[0].get('id')
        else:
            ws_id = self.workspaces.json()[0].get('id')

        self.projects = requests.get(
            url=(
                "https://www.toggl.com/api/v8/workspaces/{ws_id}/projects"
            ).format(ws_id=ws_id),
            headers={
                'Content-Type': 'application/json',
            },
            auth=(self.token, 'api_token')
        )
        return self.projects.json()

    def get_workspaces(self):
        """Get the available workspaces."""
        self.workspaces = requests.get(
            url='https://www.toggl.com/api/v8/workspaces',
            auth=(self.token, 'api_token')
        )
        workspaces = self.workspaces.json()[0]
        with open('.workspaces.json', 'w') as ws_json_file:
            ws_json_file.write(json.dumps(workspaces, indent=2))
        return self.workspaces
