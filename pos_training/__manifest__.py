{
    "name": "POS Training",
    "version": "16.0",
    "summary": "Learning Point of Sale",
    "author": "Rohit Jha",
    "sequence": "1",
    "depends": ["point_of_sale", "base"],
    "website": "https://github.com/Rohitbrainvire/School_management",
    "category": "Learning",
    "data": ["security/ir.model.access.csv",
             "views/custom_pos.xml",
             "views/location.xml",
             "views/pos_config_view.xml"],

    "assets": {
        'point_of_sale.assets': [
            "pos_training/static/src/**/*"
        ]
    },

    "installable": True,
    "application": True,

    "license": "LGPL-3",
}