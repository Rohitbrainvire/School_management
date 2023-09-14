from odoo import http

class EmployeeInformation(http.Controller):

    @http.route('/employees', auth = 'public', type = 'json', methods = ['POST'])
    def all_employees(self):
        employees = http.request.env['employee.information'].search_read([],['employee_name', 'employee_image', 'employee_phone_number', 'employee_work_exp', 'employee_city'])
        return employees