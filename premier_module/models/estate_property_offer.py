from odoo import models, fields, api
from datetime import timedelta

class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Estate Property Offer'

    name = fields.Char(
        string='Name',
        compute='_compute_name',
        store=True,
    )
    estate_property_id = fields.Many2one('estate.property', string='Estate Property')
    seller_id = fields.Many2one(
        'res.partner',
        related='estate_property_id.owner_id',
        string='Seller'
    )
    buyer_id = fields.Many2one('res.partner', string='Buyer')
    selling_price = fields.Float(string='Selling Price')
    offer_date = fields.Date(string='Offer Date')
    validity_date = fields.Date(
        string='Validity Date',
        compute='_compute_validity_date',
        inverse='_inverse_validity_date',
        search='_search_validity_date',
    )

    @api.depends('estate_property_id', 'buyer_id', 'offer_date', 'selling_price', 'seller_id')
    def _compute_name(self):
        for offer in self:
            offer.name = f'{offer.estate_property_id.name} - {offer.buyer_id.name} - {offer.offer_date} - {offer.selling_price} - {offer.seller_id.name}'
    
    @api.depends('offer_date')
    def _compute_validity_date(self):
        for offer in self:
            if offer.offer_date:
                offer.validity_date = offer.offer_date + timedelta(days=30)
    
    def _inverse_validity_date(self):
        for offer in self:
            if offer.validity_date:
                offer.offer_date = offer.validity_date - timedelta(days=30)
    
    def _search_validity_date(self, operator, value):
        if operator == 'like':
            operator = 'ilike'
        date = fields.Date.from_string(value)
        return [('offer_date', operator, date - timedelta(days=30))]
    
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('offer_date'):
                vals['offer_date'] = fields.Date.today()
        return super().create(vals_list)