from odoo import fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    is_surplus_charges = fields.Boolean(string="Is Surplus Charges?")
