from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    total_surplus_charge = fields.Char(string="Total Surplus Charge")

    def action_add_charge(self):
        wizard_view_id = self.env.ref("surplus_charges.surplus_charges_wizard_form").id

        return {
            "name": "surplus.charges.wizard",
            "type": "ir.actions.act_window",
            "view_type": "form",
            "view_mode": "form",
            "res_model": "surplus.charges.wizard",
            "view_id": wizard_view_id,
            "target": "new",
            "context": {"sale_id": self.id},
        }
