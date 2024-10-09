from odoo import models, api

class ReportEstateProperty(models.AbstractModel):
    _name = 'report.premier_module.report_estate_property'
    _description = 'Estate Property Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['estate.property'].browse(docids)
        crm_leads = self.env['crm.lead'].search([('estate_property_id', 'in', docs.ids)])
        return {
            'doc_ids': docids,
            'doc_model': 'estate.property',
            'docs': docs,
            'crm_leads': crm_leads,
        }