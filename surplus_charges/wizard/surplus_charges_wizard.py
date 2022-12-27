from odoo import fields, models


class SurplusChargesWizard(models.TransientModel):
    _name = "surplus.charges.wizard"
    _description = "surplus.charges.wizard"

    product_id = fields.Many2one("surplus.charges.configuration", string="Product")
    surplus_charges = fields.Float(
        related="product_id.surplus_charges", string="surplus_charges"
    )

    def btn_add(self):
        sale_id = self.env["sale.order"].browse(self.env.context.get("sale_id"))
        surplus_charge_sum = 0
        for rec in sale_id.order_line:
            if rec.product_id.detailed_type == "service":
                rec.unlink()
            else:
                surplus_charge_sum += rec.price_subtotal

        new_order_line = []
        line = (
            0,
            0,
            {
                "product_id": self.product_id.product_id.id,
                "price_unit": self.surplus_charges,
            },
        )
        new_order_line.append(line)

        sale_id.write(
            {
                "order_line": new_order_line,
                "total_surplus_charge": (surplus_charge_sum * self.surplus_charges)
                / 100,
            }
        )
