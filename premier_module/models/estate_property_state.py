from odoo import models, fields

class EstatePropertyState(models.Model):
    _name = 'estate.property.state'
    _description = 'Estate Property State'

    name = fields.Char(string='Name')
    is_sale = fields.Boolean(string='Is a Sale State')