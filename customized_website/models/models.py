from odoo import models, fields, api


class customized_website(models.Model):
    _name = 'customized_website.customized_website'
    _description = 'customized_website.customized_website'

    name = fields.Char()
    email = fields.Char()
    message = fields.Text()
