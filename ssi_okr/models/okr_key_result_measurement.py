# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class OkrKeyResultMeasurement(models.Model):
    _name = "okr_key_result.measurement"
    _description = "OKR Key Result - Measurement"

    key_result_id = fields.Many2one(
        string="Key Result",
        comodel_name="okr_key_result",
        required=True,
        ondelete="cascade",
    )
    user_id = fields.Many2one(
        string="User",
        comodel_name="res.users",
        required=True,
        default=lambda self: self.env.user,
    )
    date = fields.Date(
        string="Date",
        required=True,
    )
    value = fields.Float(
        string="Value",
        required=True,
    )
    note = fields.Text(
        string="Note",
    )
