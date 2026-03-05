{
    'name': 'ASP Custom',
    'version': '18.0.1.0.0',
    'category': 'Custom',
    'depends': ['product'],
    'data': [
        'security/ir.model.access.csv',
        'views/asp_brand_views.xml',
        'views/product_category_views.xml',
        'views/product_template_views.xml',
    ],
    'installable': True,
    'auto_install': False,
}