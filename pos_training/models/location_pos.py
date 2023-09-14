from odoo import fields, models, api

class PosOrderLoc(models.Model):
    _inherit = "pos.order"

    location = fields.Many2one('pos.location')

    @api.model
    def _order_fields(self, ui_order):
        res = super(PosOrderLoc, self)._order_fields(ui_order)
        loc_id = ui_order.get('selected_location')
        if loc_id:
            res['location'] = loc_id.get('id')
        return res

class Location(models.Model):
    _name = 'pos.location'
    _description = 'set location'
    _rec_name = 'location'

    location = fields.Char()

class LocationPos(models.Model):
    _inherit = 'pos.config'

    selected_location = fields.Many2many('pos.location')

class AllocateLocation(models.TransientModel):
    _inherit = 'res.config.settings'

    pos_selected_location = fields.Many2many(
        related='pos_config_id.selected_location', readonly=False)

class Session(models.Model):
    _inherit = "pos.session"

    selected_location = fields.Many2many(
        'pos.location', related='config_id.selected_location', string='loc session')

    @api.model
    def _pos_ui_models_to_load(self):
        models_to_load = super()._pos_ui_models_to_load()
        models_to_load.append('pos.location')
        return models_to_load

    def _loader_params_pos_location(self):
        return {
            'search_params': {

                'fields': [
                    'location'
                ],
            }
        }

    def _get_pos_ui_pos_location(self, params):
        dd = list(self.env['pos.location'].search_read(
            **params['search_params']))
        return dd
    
    def _loader_params_product_product(self):
        product = super()._loader_params_product_product()
        product.get('search_params').get('fields').append('qty_available')
        return product