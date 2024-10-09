from odoo import models, fields, api

class CommissionMixin(models.AbstractModel):
    _name = 'commission.mixin'
    _description = 'Commission Mixin'

    user_id = fields.Many2one('res.users', string='User', required=True)

    @api.model
    def _get_commission(self, selling_price):
        return (selling_price * 0.05)