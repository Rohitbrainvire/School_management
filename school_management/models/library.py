from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime

class LibraryManagement(models.Model):
    _name = 'school.management.library'
    _description = 'Library Management'

    name_id = fields.Many2one('school.management.student', string='Enrollment Number')
    student_name = fields.Char(string='Student Name', compute='_compute_student_name')
    librarian_id = fields.Many2one('res.users')
    issue_date = fields.Datetime(string= 'issue date and time')
    return_date = fields.Datetime()
    # book_id = fields.Many2one('')

    @api.model
    def default_get(self, fields):
        res = super(LibraryManagement, self).default_get(fields)
        res['issue_date'] = datetime.now()
        return res
        
    @api.depends('name_id')
    def _compute_student_name(self):
        for record in self:
            record.student_name = record.name_id.name



    @api.constrains('issue_date', 'return_date')
    def _check_return_date(self):
        for record in self:
            if record.issue_date and record.return_date and record.return_date < record.issue_date:
                raise ValidationError("Return date cannot be earlier than the issue date.")