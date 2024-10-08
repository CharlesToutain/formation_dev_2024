from odoo import models, fields

class EstatePropertyOwner(models.Model):
    _name = 'estate.property.owner'
    _inherits = {'res.partner': 'partner_id'}


    partner_id = fields.Many2one(
        'res.partner', 'Res Partner',
        auto_join=True, index=True, ondelete="cascade", required=True)
    
    