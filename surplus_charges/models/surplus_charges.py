from datetime import date
from odoo.exceptions import ValidationError
from odoo import api, fields, models


class SurplusChargesConfiguration(models.Model):
    _name = "surplus.charges.configuration"
    _rec_name = "product_id"
    _description = "Configure Surplus Charges for SO"

    product_id = fields.Many2one(
        "product.product",
        string="Product",
        domain="[('is_surplus_charges','=',True),('detailed_type','=','service')]",
    )
    surplus_charges = fields.Float(string="surplus_charges")
    active = fields.Boolean(string="Is Active?")
    start_date = fields.Date(string="start_date")
    end_date = fields.Date(string="end_date")
    display_name = fields.Char(compute="compute_display_name", string="Display Name?")

    _sql_constraints = [
        (
            "product_id",
            "UNIQUE(product_id)",
            "There must be a unique product_id per record",
        )
    ]

    @api.onchange("surplus_charges")
    def check_surplus_percentage(self):
        if 0 <= self.surplus_charges <= 100:
            pass
        else:
            raise ValidationError("surplus charge should be between 0 and 100 ")

    @api.onchange("start_date")
    def check_start_date(self):
        current_date = date.today()
        for rec in self:
            if rec.start_date:
                if rec.start_date < current_date:
                    raise ValidationError(
                        "start date cannot be smaller than or equal to Today's date"
                    )

    @api.onchange("end_date")
    def check_end_date(self):
        for rec in self:
            if rec.start_date:
                if rec.end_date < rec.start_date:
                    raise ValidationError("End Date cannot be smaller than Start date")

    @api.depends("product_id", "surplus_charges")
    def compute_display_name(self):
        for rec in self:
            if rec.product_id and rec.surplus_charges:
                rec.display_name = "%s - %s" % (
                    rec.product_id.name,
                    rec.surplus_charges,
                )
            else:
                rec.display_name = "New"
