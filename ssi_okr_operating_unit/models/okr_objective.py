# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl-3.0-standalone.html).

from odoo import models


class OkrObjective(models.Model):
    """
    Attaches ``mixin.single_operating_unit`` to the OKR objective model.
    Adds the Operating Unit field to objectives and enforces the record
    rules that scope objective access by Operating Unit.
    """

    _name = "okr_objective"
    _inherit = [
        "okr_objective",
        "mixin.single_operating_unit",
    ]
