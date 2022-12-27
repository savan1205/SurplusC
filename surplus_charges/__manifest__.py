{
    "name": "Surplus Charges Configuration",
    "version": "15.0.1.0.1",
    "summary": "surplus_charges_configuration",
    "sequence": 1,
    "description": """
        This module contains all the features of Configuring Sales Orders to add Surplus Charges to them.
    """,
    "depends": ["sale_management"],
    "data": [
        "security/security_groups.xml",
        "security/ir.model.access.csv",
        "views/surplus_charges_views.xml",
        "views/product_views.xml",
        "views/sale_order_views.xml",
        "wizard/surplus_charges_wizard_views.xml",
    ],
    "demo": [],
    "installable": True,
    "application":True,
    "auto_install": False,
    "license": "LGPL-3",
}
