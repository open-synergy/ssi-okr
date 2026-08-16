# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl-3.0-standalone.html).

from odoo import models


class OkrKeyResult(models.Model):
    """
    Attaches ``mixin.single_operating_unit`` to the OKR key result model.
    Adds the Operating Unit field to key results and enforces the record
    rules that scope key result access by Operating Unit.
    """

    _name = "okr_key_result"
    _inherit = [
        "okr_key_result",
        "mixin.single_operating_unit",
    ]
