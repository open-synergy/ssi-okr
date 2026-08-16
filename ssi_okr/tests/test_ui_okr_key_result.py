# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# HttpSavepointCase -- NOT HttpCase. In 14.0 only SavepointCase prepares
# ``cls.env`` in ``setUpClass``, which is where every work instruction
# Pre-Condition below is built.
from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiOkrKeyResult(HttpSavepointCase):
    """Tour tests for the ``okr_key_result`` work instructions."""

    @classmethod
    def setUpClass(cls):
        """Create one Key Result per tour, in the state its IK requires.

        ``base.user_admin`` is already a member of
        ``okr_key_result_validator_group`` (which implies the ``User``
        and ``Viewer`` groups) and of ``okr_key_result_all`` through
        ``security/res_groups/okr_key_result.xml``, so it can run every
        tour below and can see every fixture. Each Key Result still gets
        an explicit ``user_id`` so that the record rule
        ``okr_key_result_internal_user_rule`` cannot hide it from the
        tour session.
        """
        super().setUpClass()
        cls.admin = cls.env.ref("base.user_admin")

        # Pre-Condition 10-cancel.md: the wizard lists the reasons of
        # ``ir.model.all_cancel_reason_ids``, so the fixture must be
        # global to show up regardless of demo data.
        cls.cancel_reason = (
            cls.env["base.cancel_reason"]
            .with_user(cls.admin)
            .create(
                {
                    "name": "Tour OKR KR Cancel Reason",
                    "code": "TOURKRCR",
                    "global_use": True,
                }
            )
        )

        # Pre-Condition 01-create.md: the Unit of Measure the create tour
        # picks from the dropdown. A dedicated category plus its own
        # reference unit keeps the name unique, so ``:contains`` can never
        # land on a demo unit.
        cls.uom_category = cls.env["uom.category"].create(
            {"name": "Tour OKR KR Category"}
        )
        cls.uom = cls.env["uom.uom"].create(
            {
                "name": "Tour OKR KR Unit",
                "category_id": cls.uom_category.id,
                "uom_type": "reference",
                "factor": 1.0,
            }
        )

        # Pre-Condition 01-create.md: a parent Objective whose Partner is
        # empty, so it matches the Objective field domain while the create
        # tour leaves Partner untouched.
        #
        # The document number is assigned manually here on purpose:
        # ``mixin.transaction.name_get`` returns ``"*<id>"`` while ``name``
        # is still the ``/`` placeholder, so a Draft Objective could not be
        # typed into the ``objective_id`` autocomplete at all.
        cls.objective = (
            cls.env["okr_objective"]
            .with_user(cls.admin)
            .create(
                {
                    "name": "TOUR-OKR-OBJ",
                    "objective": "Tour OKR Key Result Parent Objective",
                    "date_start": "2026-01-01",
                    "date_end": "2026-12-31",
                    "user_id": cls.admin.id,
                }
            )
        )

        # Pre-Condition 08-ready.md: Draft.
        cls.key_result_ready = cls._create_key_result("Ready")

        # Pre-Condition 07-start.md: Ready to Process.
        cls.key_result_start = cls._create_key_result("Start")
        cls._run_transition(cls.key_result_start, "action_ready")

        # Pre-Condition 04-confirm.md: On Progress.
        cls.key_result_confirm = cls._create_key_result("Confirm")
        cls._run_transition(cls.key_result_confirm, "action_ready")
        cls._run_transition(cls.key_result_confirm, "action_open")

        # Pre-Condition 05-approve.md: Waiting for Approval, with
        # ``admin`` among the record's active approvers -- the standard
        # approval.template routes approval to
        # ``okr_key_result_validator_group``.
        cls.key_result_approve = cls._create_key_result("Approve")
        cls._run_transition(cls.key_result_approve, "action_ready")
        cls._run_transition(cls.key_result_approve, "action_open")
        cls._run_transition(cls.key_result_approve, "action_confirm")

        # Pre-Condition 10-cancel.md: Draft, one of the states the
        # cancel policy allows.
        cls.key_result_cancel = cls._create_key_result("Cancel")

    @classmethod
    def _create_key_result(cls, label):
        """Create one Draft Key Result dedicated to a single tour.

        :param label: short scenario name, e.g. ``"Confirm"``
        :return: the new ``okr_key_result`` record, in Draft, whose
            ``key_result`` text is the key the tour uses to find its row
        """
        return (
            cls.env["okr_key_result"]
            .with_user(cls.admin)
            .create(
                {
                    "objective_id": cls.objective.id,
                    "key_result": "Tour OKR Key Result %s" % label,
                    "date": "2026-01-01",
                    "date_deadline": "2026-12-31",
                    "target_value": 100.0,
                    "uom_id": cls.uom.id,
                    "user_id": cls.admin.id,
                }
            )
        )

    @classmethod
    def _run_transition(cls, key_result, method):
        """Advance a fixture Key Result to the next state.

        The policy fields guarding each button are computed from
        ``policy.template`` against the state written by the previous
        transition, so the cache is dropped before every call.

        :param key_result: the ``okr_key_result`` record to advance
        :param method: name of the workflow method, e.g.
            ``"action_confirm"``
        """
        key_result.invalidate_cache()
        getattr(
            key_result.with_user(cls.admin).with_context(bypass_policy_check=True),
            method,
        )()

    def test_create(self):
        """Run the create tour for ``okr_key_result``.

        IK: docs/okr_key_result/01-create.md
        """
        self.start_tour(
            "/web",
            "ssi_okr_okr_key_result_create",
            login="admin",
        )

    def test_ready(self):
        """Run the stage tour for ``okr_key_result``.

        IK: docs/okr_key_result/08-ready.md
        """
        self.start_tour(
            "/web",
            "ssi_okr_okr_key_result_ready",
            login="admin",
        )

    def test_start(self):
        """Run the start tour for ``okr_key_result``.

        IK: docs/okr_key_result/07-start.md
        """
        self.start_tour(
            "/web",
            "ssi_okr_okr_key_result_start",
            login="admin",
        )

    def test_confirm(self):
        """Run the confirm tour for ``okr_key_result``.

        IK: docs/okr_key_result/04-confirm.md
        """
        self.start_tour(
            "/web",
            "ssi_okr_okr_key_result_confirm",
            login="admin",
        )

    def test_approve(self):
        """Run the approve tour for ``okr_key_result``.

        IK: docs/okr_key_result/05-approve.md
        """
        self.start_tour(
            "/web",
            "ssi_okr_okr_key_result_approve",
            login="admin",
        )

    def test_cancel(self):
        """Run the cancel tour for ``okr_key_result``.

        IK: docs/okr_key_result/10-cancel.md
        """
        self.start_tour(
            "/web",
            "ssi_okr_okr_key_result_cancel",
            login="admin",
        )
