from odoo import models, fields, api

class MassOffer(models.TransientModel):
    _name = 'mass.offer'
    _description = 'Mass Offer Wizard'

    buyer_id = fields.Many2one('res.partner', string='Buyer')
    offer_lines_ids = fields.One2many('mass.offer.line', 'offer_id', string='Offer Lines')


class MassOfferLine(models.TransientModel):
    _name = 'mass.offer.line'
    _description = 'Mass Offer Line'

    offer_id = fields.Many2one('mass.offer', string='Offer')
    estate_property_id = fields.Many2one('estate.property', string='Property')
    seller_id = fields.Many2one(
        'res.partner',
        related='estate_property_id.owner_id',
        string='Seller'
    )
    selling_price = fields.Float(string='Selling Price')
    price = fields.Float(
        string='Value Price',
        related='estate_property_id.price'
    )
