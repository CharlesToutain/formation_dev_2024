from odoo import models, fields, api

class EstateProperty(models.Model):
    _name = 'estate.property'
    _inherit = ['image.mixin']
    _description = 'Estate Property'

    _sql_constraints = [
        ('check_name_unique', 'UNIQUE(name)', 'The name of the property must be unique')
    ]
    
  
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
    offer_ids = fields.One2many('estate.property.offer', 'estate_property_id', string='Offers')
    tag_ids = fields.Many2many('estate.property.tag', string='Tags')


    @api.model
    def create(self, vals):
        if not vals.get('description'):
            vals['description'] = 'lorem ipsum'
        return super().create(vals)

    @api.onchange('city', 'zip', 'country_id', 'street')
    def onchange_city(self):
        if self.city or self.zip or self.country_id or self.street:
            self.description += f'{self.street} {self.zip} {self.city} {self.country_id.name}'
    