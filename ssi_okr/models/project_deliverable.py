# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import fields, models


class ProjectDeliverable(models.Model):
    _name = "project_deliverable"
    _inherit = [
        "project_deliverable",
    ]

    key_result_ids = fields.Many2many(
        comodel_name="okr_key_result",
        string="Key Results",
        help="Key Results related to the Deliverable.",
        relation="rel_okr_key_result_2_deliverable",
        column1="deliverable_id",
        column2="okr_key_result_id",
    )
