"""Get time entries from Toggl."""

class ToggleEntries(object):
    """Class for getting and processing Toggl entries."""
    entries = {}
    user = {}

    def get_user(self):
        """Get the user who we're interested in."""
        return self.user

    def get_current_timer(self):
        """Check for a running timer."""
        return self.entries

    def get_active_projects(self):
        """Add active projects."""
        return self.user
