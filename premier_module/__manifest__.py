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
    'depends': ['base', 'contacts'],
    'data': [
        #SECURITY
        'security/ir.model.access.csv',
        #VIEWS
        'views/estate_property_views.xml',
        'views/estate_property_state_views.xml',
        'views/estate_property_offer_views.xml',
        'views/menu.xml',
    ],
    'demo': [
        # List of demo data files
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}