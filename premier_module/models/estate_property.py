from odoo import models, fields, api

class EstateProperty(models.Model):
    _name = 'estate.property'
    _inherit = ['image.mixin']
    _description = 'Estate Property'
    
  
    name = fields.Char(
        string='Name',
        required=True,
    )
    country_id = fields.Many2one('res.country', string='Country')
    street = fields.Char(string='Street')
    zip = fields.Char(string='Postal Code')
    city = fields.Char(string='City')
    price = fields.Float(string='Price')
    type = fields.Selection([
        ('appartement', 'Appartement'),
        ('maison', 'Maison'),
        ('immeuble', 'Immeuble'),
        ('terrain', 'Terrain')
    ], string='Type', required=True)
    superficie = fields.Float(string='Area')
    nb_floor = fields.Integer(string='Number of Floors')
    description = fields.Html(string='Description')
    owner_id = fields.Many2one('res.partner', string='Owner')
    image_1920 = fields.Image(string='Picture')
    state_id = fields.Many2one('estate.property.state', string='State')