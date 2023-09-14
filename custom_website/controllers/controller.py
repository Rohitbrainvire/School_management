from odoo import http
# from odoo.http import request


class WebController(http.Controller):
    @http.route(['/dynamic'],type = 'http', auth="public")
    def load_data(self):
        controller_obj = http.request.env['controller'].search([])
        vals = {}
        for obj in controller_obj:
            vals[obj.id] = {'name' : obj.name}
        print(vals)
        return http.request.render("custom.website.dynamic", {'objects' : vals})
