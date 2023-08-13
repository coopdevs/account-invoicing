from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    self_invoice_prefix = fields.Char(
        string="Default Self Billing prefix",
        help="Self Billing prefix for Bills generated by this company",
    )