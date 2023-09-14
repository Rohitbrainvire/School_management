{
    'name': 'website work',
    'version': '1.0',
    'category': 'Apps',
    
    'author': 'Ashish singh',
    'depends': ['base','web','website'],
    
    'assets': {
        'web.assets_backend': [
            'custom_website/static/src/**/*',
        ],
    },
    'data': [
        "security/ir.model.access.csv",
        "views/model.xml",
        "views/dynamic_tem.xml"
    ],
    # 'assets': {
    #     'point_of_sale.assets': [
    #         "pos_order/static/src/**/*",
    #     ],
    #     },
    "application": True,
    
    "sequence": 1
}