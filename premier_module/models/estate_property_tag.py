from __future__ import annotations
from random import randint
from odoo import models, fields, api

class EstatePropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = 'Estate Property Tag'
    _order = 'name'
    _parent_name = 'parent_id'
    _parent_store = True

    def _get_default_color(self):
        return randint(1, 11)

    name = fields.Char(string='Name', required=True, translate=True)
    color = fields.Integer(
        string='Color Index',
        default=_get_default_color,
    )
    parent_id: EstatePropertyTag = fields.Many2one('estate.property.tag', string='Category', index=True, ondelete='cascade')
    child_ids: EstatePropertyTag = fields.One2many('estate.property.tag', 'parent_id', string='Child Tags')
    parent_path = fields.Char(index=True)
    active = fields.Boolean(string='Active', default=True)

    @api.depends('parent_id')
    def _compute_display_name(self):
        """ Return the categories' display name, including their direct
            parent by default.
        """
        for category in self:
            names = []
            current = category
            while current:
                names.append(current.name or "")
                current = current.parent_id
            category.display_name = ' / '.join(reversed(names))
            
