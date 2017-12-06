"""Model for saving timesheets for projects."""
import sqlalchemy as sql

from sqlalchemy.ext.declarative import declarative_base


class Project(declarative_base()):
    """Model class for saving timesheets."""
    __tablename__ = 'project_project'
    id = sql.Column(sql.types.Integer, primary_key=True)
    children = sql.orm.relationship('timesheet')

    def __init__(self):
        sql.create_engine('postgresql://duchess@psql:4096/gcorp-dev?ssl')

    def save_timesheet(self):
        """Save an entry."""
        return self.timesheet

    def get_timesheet(self):
        """Load a time entry."""
        return self.timesheet
