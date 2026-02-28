# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl-3.0-standalone.html).

from odoo import models


class OkrKeyResult(models.Model):
    _name = "okr_key_result"
    _inherit = [
        "okr_key_result",
        "mixin.single_operating_unit",
    ]
