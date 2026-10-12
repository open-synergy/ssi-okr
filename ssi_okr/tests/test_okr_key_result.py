# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestOkrKeyResult(YamlTransactionCase):
    """Cover the ``okr_key_result`` type, frequency and assessment."""

    def test_okr_key_result_assessment(self):
        """Run the ``test_data_okr_key_result.yaml`` scenarios."""
        self.run_yaml_scenario("test_data_okr_key_result.yaml")
