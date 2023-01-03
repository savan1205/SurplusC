from odoo import api, fields, models


class ProductBrand(models.Model):
    _name = "product.brand"

    name = fields.Char(string="Brand")
    product_ids = fields.One2many(comodel_name="product.template", inverse_name="brand_id",
                                    string="Product")




