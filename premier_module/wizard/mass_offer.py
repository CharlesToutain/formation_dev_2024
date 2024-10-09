from odoo import models, fields, api
from odoo.exceptions import ValidationError

class MassOffer(models.TransientModel):
    _name = 'mass.offer'
    _description = 'Mass Offer Wizard'

    buyer_id = fields.Many2one('res.partner', string='Buyer')
    offer_lines_ids = fields.One2many('mass.offer.line', 'offer_id', string='Offer Lines')


    def create_offers(self):
        vals = []
        for line in self.offer_lines_ids:
            vals.append({
                'estate_property_id': line.estate_property_id.id,
                'buyer_id': self.buyer_id.id,
                'selling_price': line.selling_price,
            })
        self.env['estate.property.offer'].create(vals)
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'estate.property.offer',
            'view_mode': 'list,form',
            'context': {'search_default_buyer': self.buyer_id.id},
        }


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

    @api.constrains('selling_price')
    def _check_selling_price(self):
        for line in self:
            if line.selling_price <= 0:
                raise ValidationError('The selling price must be positive')