from odoo import http
from odoo.http import request

class MyController(http.Controller):

    @http.route('/my_custom_page', auth='public', website=True)
    def my_custom_page(self, **kw):
        record  = request.render('customized_website.custom_page_template')
        return record
    
    @http.route('/my_custom_page/data', auth="user", type="json", methods=['POST'])
    def form_data(self, **kw):
   
        print(kw)
        
        request.env['customized_website.customized_website'].create([kw])
        
        return True