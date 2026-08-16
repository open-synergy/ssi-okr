# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# HttpSavepointCase -- NOT HttpCase. In 14.0 only SavepointCase prepares
# ``cls.env`` in ``setUpClass``, which is where every work instruction
# Pre-Condition below is built.
from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiOkrObjective(HttpSavepointCase):
    """Tour tests for the ``okr_objective`` work instructions."""

    @classmethod
    def setUpClass(cls):
        """Create one Objective per tour, in the state its IK requires.

        ``base.user_admin`` is already a member of
        ``okr_objective_validator_group`` (which implies the ``User``
        and ``Viewer`` groups) and of ``okr_objective_all`` through
        ``security/res_groups/okr_objective.xml``, so it can run every
        tour below and can see every fixture. Each Objective still gets
        an explicit ``user_id`` so that the record rule
        ``okr_objective_internal_user_rule`` cannot hide it from the
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
                    "name": "Tour OKR Cancel Reason",
                    "code": "TOUROKRCR",
                    "global_use": True,
                }
            )
        )

        # Pre-Condition 01-create.md: nothing to prepare -- the tour
        # creates the Objective itself.

        # Pre-Condition 08-ready.md: Draft.
        cls.objective_ready = cls._create_objective("Ready")

        # Pre-Condition 07-start.md: Ready to Process.
        cls.objective_start = cls._create_objective("Start")
        cls._run_transition(cls.objective_start, "action_ready")

        # Pre-Condition 04-confirm.md: On Progress.
        cls.objective_confirm = cls._create_objective("Confirm")
        cls._run_transition(cls.objective_confirm, "action_ready")
        cls._run_transition(cls.objective_confirm, "action_open")

        # Pre-Condition 05-approve.md: Waiting for Approval, with
        # ``admin`` among the record's active approvers -- the standard
        # approval.template routes approval to
        # ``okr_objective_validator_group``.
        cls.objective_approve = cls._create_objective("Approve")
        cls._run_transition(cls.objective_approve, "action_ready")
        cls._run_transition(cls.objective_approve, "action_open")
        cls._run_transition(cls.objective_approve, "action_confirm")

        # Pre-Condition 10-cancel.md: Draft, one of the states the
        # cancel policy allows.
        cls.objective_cancel = cls._create_objective("Cancel")

    @classmethod
    def _create_objective(cls, label):
        """Create one Draft Objective dedicated to a single tour.

        :param label: short scenario name, e.g. ``"Confirm"``
        :return: the new ``okr_objective`` record, in Draft, whose
            ``objective`` text is the key the tour uses to find its row
        """
        return (
            cls.env["okr_objective"]
            .with_user(cls.admin)
            .create(
                {
                    "objective": "Tour OKR Objective %s" % label,
                    "date_start": "2026-01-01",
                    "date_end": "2026-12-31",
                    "user_id": cls.admin.id,
                }
            )
        )

    @classmethod
    def _run_transition(cls, objective, method):
        """Advance a fixture Objective to the next state.

        The policy fields guarding each button are computed from
        ``policy.template`` against the state written by the previous
        transition, so the cache is dropped before every call.

        :param objective: the ``okr_objective`` record to advance
        :param method: name of the workflow method, e.g.
            ``"action_confirm"``
        """
        objective.invalidate_cache()
        getattr(
            objective.with_user(cls.admin).with_context(bypass_policy_check=True),
            method,
        )()

    def test_create(self):
        """Run the create tour for ``okr_objective``.

        IK: docs/okr_objective/01-create.md
        """
        self.start_tour(
            "/web",
            "ssi_okr_okr_objective_create",
            login="admin",
        )

    def test_ready(self):
        """Run the stage tour for ``okr_objective``.

        IK: docs/okr_objective/08-ready.md
        """
        self.start_tour(
            "/web",
            "ssi_okr_okr_objective_ready",
            login="admin",
        )

    def test_start(self):
        """Run the start tour for ``okr_objective``.

        IK: docs/okr_objective/07-start.md
        """
        self.start_tour(
            "/web",
            "ssi_okr_okr_objective_start",
            login="admin",
        )

    def test_confirm(self):
        """Run the confirm tour for ``okr_objective``.

        IK: docs/okr_objective/04-confirm.md
        """
        self.start_tour(
            "/web",
            "ssi_okr_okr_objective_confirm",
            login="admin",
        )

    def test_approve(self):
        """Run the approve tour for ``okr_objective``.

        IK: docs/okr_objective/05-approve.md
        """
        self.start_tour(
            "/web",
            "ssi_okr_okr_objective_approve",
            login="admin",
        )

    def test_cancel(self):
        """Run the cancel tour for ``okr_objective``.

        IK: docs/okr_objective/10-cancel.md
        """
        self.start_tour(
            "/web",
            "ssi_okr_okr_objective_cancel",
            login="admin",
        )
