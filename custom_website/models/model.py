from odoo import models, fields

class ContModel(models.Model):
    _name = "controller"
    _description = "testing controller"

    name = fields.Char()
    img = fields.Binary()