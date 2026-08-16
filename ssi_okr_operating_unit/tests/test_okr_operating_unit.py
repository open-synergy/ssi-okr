# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestOkrOperatingUnit(YamlTransactionCase):
    """Covers the Operating Unit fields on ``okr_objective`` and
    ``okr_key_result``."""

    def test_okr_operating_unit(self):
        """Run the Operating Unit scenario for OKR objective/key result."""
        self.run_yaml_scenario("test_data_okr_operating_unit.yaml")
