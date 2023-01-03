

{
    "name": "Surplus Charges Configuration",
    "version": "15.0.1.0.1",
    "summary": "configure extra/surplus charges for SO",
    "sequence": 1,
    "description": """
        This module contains all the features of Configuring Sales Orders to add Surplus Charges to them.
    """,
    "depends": ["sale_management","website_sale"],
    "data": [
        "security/security_groups.xml",
        "security/ir.model.access.csv",


        "views/brand_web_view.xml",
        "views/surplus_charges_views.xml",
        "views/product_brand_views.xml",
        "views/product_views.xml",
        "views/sale_order_views.xml",
        "data/brand_web_menu.xml",

        "wizard/surplus_charges_wizard_views.xml",
    ],
    "demo": [],
    "installable": True,
    "application":True,
    "auto_install": False,
    "license": "LGPL-3",

    # 'assets':{
    #     'web.assets_frontend':[
    #         'surplus_charges/static/src/css/brand.css'
    #     ]
    #
    # }
}
