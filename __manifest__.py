{
    'name': 'Algolia eCommerce Search Integration',
    'version': '1.0',
    'summary': 'Integrates Algolia search engine with Odoo Version 16 Community Edition eCommerce.',
    'sequence': 10,
    'license': 'LGPL-3',
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'category': 'Website',
    'depends': ['website_sale'],
    'data': [
        'views/algolia_settings.xml',
        'views/search_template.xml',
        'views/search_results_page.xml',
        'views/responsive_design.xml',
        'data/algolia_data.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'assets': {
        'web.assets_frontend': [
            'static/src/js/search_autocomplete.js',
            'static/src/js/search_filters.js',
            'static/src/css/search_styles.css',
        ],
        'web.assets_qweb': [
            'static/src/xml/*.xml',
        ],
    },
}