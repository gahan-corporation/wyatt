"""Test cases for the Timesheet model."""
import timesheets.timesheet as timesheet


class TestTimesheet(object):
    """Test Timesheet class."""
    timesheet = timesheet.Timesheet()

    def test_timesheet_instance(self):
        """Test that we can instantiate a timesheet correctly."""
        timesheet_type = type(timesheet.Timesheet())
        local_timesheet = timesheet.Timesheet()
        print(type(self.timesheet))
        print(type(timesheet))
        assert isinstance(local_timesheet, timesheet_type)

    def test_other_thing(self):
        """Some other thing."""
        return self.timesheet
