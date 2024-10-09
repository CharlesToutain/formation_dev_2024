{
    'name': 'Premier Module',
    'version': '1.0',
    'summary': 'A brief summary of the module',
    'description': """
        A detailed description of the module.
    """,
    'author': 'Your Name',
    'website': 'http://www.yourwebsite.com',
    'category': 'Uncategorized',
    'depends': ['base', 'contacts', 'crm'],
    'data': [
        #SECURITY
        'security/ir.model.access.csv',
        #DATA
        'data/res_groups.xml',
        'data/ir_rule.xml',
        'data/estate_property_state.xml',
        'data/ir_cron.xml',
        #VIEWS
        'views/estate_property_views.xml',
        'views/estate_property_state_views.xml',
        'views/estate_property_offer_views.xml',
        'views/estate_property_tag_views.xml',
        'views/crm_lead_views.xml',
        'views/res_partner.xml',
        #REPORT
        'report/report_estate_property.xml',
        # WIZARD
        'wizard/mon_super_wizard_views.xml',
        'wizard/mass_offer_views.xml',
        #MENU
        'views/menu.xml',
    ],
    'demo': [
        # List of demo data files
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}