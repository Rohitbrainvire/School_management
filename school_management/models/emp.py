from odoo import models, fields

class Employees(models.Model):
    _name = 'employee.information'
    _description = 'Employee Information'


    employee_name = fields.Char(string='Emp Name')
    employee_image = fields.Binary(string='Emp Image')
    employee_phone_number = fields.Char(string='Emp Phone Number')
    employee_work_exp = fields.Char(string='Emp Work')
    employee_city = fields.Char(string='Emp City')