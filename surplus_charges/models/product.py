from odoo import api, fields, models

class ProductTemplate(models.Model):
    _inherit = "product.template"

    brand_id = fields.Many2one(comodel_name="product.brand", string="Brand")

class ProductProduct(models.Model):
    _inherit = "product.product"

    is_surplus_charges = fields.Boolean(string="Is Surplus Charges?")
