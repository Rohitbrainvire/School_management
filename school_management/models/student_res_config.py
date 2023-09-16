from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    principal_name = fields.Char(string='Principal Name')
    
    def set_values(self):
        super(ResConfigSettings, self).set_values()
        config_param = self.env['ir.config_parameter'].sudo()
        self.env['school.management.student'].sudo().search([]).write({'name': self.principal_name})
        config_param.set_param('school_management.principal_name', self.principal_name)
       
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        config_param = self.env['ir.config_parameter'].sudo()
        res.update(
            principal_name=config_param.get_param('school_management.principal_name', default=True),
        )

        return res
    
   
        
