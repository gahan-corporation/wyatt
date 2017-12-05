"""Model for saving timesheets for projects."""
import sqlalchemy as sql

from sqlalchemy.ext.declarative import declarative_base


class Timesheet(declarative_base()):
    """Model class for saving timesheets."""
    __tablename__ = 'gerp_timesheets'
    tid = sql.Column(sql.types.Integer, primary_key=True)
    description = sql.Column(sql.types.Text)
    duration = sql.Column(sql.types.String)
    start = sql.Column(sql.types.DateTime)
    stop = sql.Column(sql.types.DateTime)
    task_id = sql.Column(sql.types.Integer, sql.ForeignKey('task.id'))
    toggl_id = sql.Column(sql.types.String)
    project_id = sql.Column(sql.types.Integer, sql.ForeignKey('project.id'))
    partner_id = sql.Column(sql.types.Integer, sql.ForeignKey('partner.id'))
    timesheet = {}

    def __init__(self):
        engine = sql.create_engine(
            'postgresql://duchess@psql:4096/gcorp-dev?ssl')
        session_maker = sql.orm.sessionmaker(bind=engine)
        self.session = session_maker()

    def save_time_entry(self):
        """This should fill in as many of the fields as possible."""
        return self.session

    def delete_time_entry(self):
        """Save an entry."""
        print(self.session.dirty)
        return self.timesheet

    def get_time_entry(self):
        """Load a time entry."""
        return self.timesheet
