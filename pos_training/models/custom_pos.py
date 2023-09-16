from odoo import models, fields,api

class PosOrder(models.Model):
    _inherit = "pos.order"

    note = fields.Char(string="order note")

    @api.model
    def _order_fields(self,ui_order):
        new_data=super(PosOrder,self)._order_fields(ui_order)
        new_data['note']=ui_order.get("json_note")
        return new_data
    
class PhonePOS(models.Model):
    _inherit = "res.partner"
    
    phone_number = fields.Char()
    
class POS(models.Model):
    _inherit = "pos.session"
    
    def _loader_params_res_partner(self):
        result= super()._loader_params_res_partner()
        result.get('search_params').get('fields').append('phone_number')
        return result