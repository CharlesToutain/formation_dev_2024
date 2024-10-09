from odoo import api, fields, models

class MonSuperWizard(models.TransientModel):
    _name = 'mon.super.wizard'
    _description = 'Mon Super Wizard'

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')

    @api.model
    def default_get(self, fields):
        res = super(MonSuperWizard, self).default_get(fields)
        # Add default values if needed
        return res

    def action_confirm(self):
        # Add your logic for the confirm action
        return {'type': 'ir.actions.act_window_close'}