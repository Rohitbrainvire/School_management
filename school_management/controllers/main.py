from odoo import http
from odoo.http import request


class Hello(http.Controller):
    @http.route('/rohit/jha/', website=True, auth='public')
    def know_ledge(self, **kw):
        # return "Hello, World"
        students = request.env['school.management.student'].search([])
        return request.render("school_management.new_page", {
            'students': students
        })
