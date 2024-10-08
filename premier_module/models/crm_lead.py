from __future__ import annotations
from odoo import models, fields

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    estate_property_id: CrmLead = fields.Many2one('estate.property', string='Property')
    

    def action_set_won_rainbowman(self):
        res = super().action_set_won_rainbowman()
        if not self.estate_property_id:
            self.estate_property_id = self.env['estate.property'].create({
                'name': self.name,
                'owner_id': self.partner_id.id,
                'street': self.street,
                'zip': self.zip,
                'city': self.city,
                'country_id': self.country_id.id,
            }).id
        return res