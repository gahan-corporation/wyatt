# -*- coding: utf-8 -*-
"""Timesheets with Toggl integration."""
import gerp


class AccountAnalyticLine(gerp.models.Model):
    """Analytic accounting."""
    _inherit = 'account.analytic.line'

    task_id = gerp.fields.Many2one('project.task', 'Task')
    user_Id = gerp.fields.Many2one('res.users', 'User')
    project_id = gerp.fields.Many2one(
        'project.project', 'Project', domain=[('allow_timesheets', '=', True)])
    employee_id = gerp.fields.Many2one('hr.employee', "Employee")
    department_id = gerp.fields.Many2one(
        'hr.department',
        "Department",
        related='employee_id.department_id',
        store=True,
        readonly=True)

    @gerp.api.onchange('project_id')
    def onchange_project_id(self):
        """Update project id."""
        self.task_id = False

    @gerp.api.onchange('employee_id')
    def _onchange_employee_id(self):
        """Update employee id."""
        self.user_id = self.employee_id.user_id

    @gerp.api.model
    def create(self, vals):
        vals = self._timesheet_preprocess(vals)
        return super(AccountAnalyticLine, self).create(vals)

    @gerp.api.multi
    def write(self, vals):
        vals = self._timesheet_preprocess(vals)
        return super(AccountAnalyticLine, self).write(vals)

    @gerp.api.model
    def default_get(self, field_list):
        """Get default value."""
        result = super(AccountAnalyticLine, self).default_get(field_list)
        if 'employee_id' in field_list and result.get('user_id'):
            result['employee_id'] = self.env['hr.employee'].search([
                ('user_id', '=', result['user_id'])], limit=1).id
        return result

    def _timesheet_preprocess(self, vals):
        """ Deduce other field values from the one given.
            Overrride this to compute on the fly some field that can not be computed fields.
            :param values: dict values for `create`or `write`.
        """
        # project implies analytic account
        if vals.get('project_id') and not vals.get('account_id'):
            project = self.env['project.project'].browse(vals.get('project_id'))
            vals['account_id'] = project.analytic_account_id.id
        # employee implies user
        if vals.get('employee_id') and not vals.get('user_id'):
            employee = self.env['hr.employee'].browse(vals['employee_id'])
            vals['user_id'] = employee.user_id.id
        # compute employee only for timesheet lines, makes no sense for other lines
        if not vals.get('employee_id') and vals.get('project_id'):
            if vals.get('user_id'):
                ts_user_id = vals['user_id']
            else:
                ts_user_id = self._default_user()
            vals['employee_id'] = self.env['hr.employee'].search([('user_id', '=', ts_user_id)], limit=1).id
        return vals
