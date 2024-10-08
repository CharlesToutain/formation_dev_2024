from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'


    estate_property_ids = fields.One2many('estate.property', 'owner_id', string='Properties')
    count_estate_properties = fields.Integer(string='Property Count', compute='_compute_count_estate_properties')


    def _compute_count_estate_properties(self):
        for partner in self:
            partner.count_estate_properties = len(partner.estate_property_ids)


    # def action_view_properties(self):
    #     action = self.env.ref('premier_module.action_estate_property').read()[0]
    #     action['domain'] = [('owner_id', '=', self.id)]
    #     action['context'] = {
    #         'default_owner_id': self.id,
    #     }
    #     return action

    def action_view_properties(self):
        if len(self.estate_property_ids) == 1:
            return {
                'type': 'ir.actions.act_window',
                'name': 'Property',
                'res_model': 'estate.property',
                'view_mode': 'form',
                'context': {
                    'default_owner_id': self.id,
                },
                'res_id': self.estate_property_ids.id,
            }
        return {
            'type': 'ir.actions.act_window',
            'name': 'Properties',
            'res_model': 'estate.property',
            'view_mode': 'list,form',
            'context': {
                'default_owner_id': self.id,
            },
            'domain': [('id', 'in', self.estate_property_ids.ids)],
        }