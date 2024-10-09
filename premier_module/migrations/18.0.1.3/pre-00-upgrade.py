# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo.upgrade import util
from odoo import api, SUPERUSER_ID


def migrate(cr, version):
    env = api.Environment(cr, SUPERUSER_ID, {})
    import pdb; pdb.set_trace()
    util.rename_field(env.cr, 'estate.property', 'description', 'new_description')
