# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "OKR + Operating Unit",
    "version": "14.0.1.1.0",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "ssi_okr",
        "ssi_operating_unit_mixin",
    ],
    "data": [
        "security/res_group/okr_objective.xml",
        "security/res_group/okr_key_result.xml",
        "security/ir_rule/okr_objective.xml",
        "security/ir_rule/okr_key_result.xml",
        "view/okr_objective.xml",
        "view/okr_key_result.xml",
    ],
    "demo": [],
}
