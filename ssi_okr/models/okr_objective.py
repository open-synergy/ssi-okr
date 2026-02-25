# Copyright 2025 OpenSynergy Indonesia
# Copyright 2025 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from datetime import date

from odoo import api, fields, models

from odoo.addons.ssi_decorator import ssi_decorator


class OkrObjective(models.Model):
    _name = "okr_objective"
    _description = "OKR Objective"
    _inherit = [
        "mixin.transaction_ready",
        "mixin.transaction_open",
        "mixin.transaction_confirm",
        "mixin.transaction_done",
        "mixin.transaction_cancel",
        "mixin.transaction_terminate",
        "mixin.many2one_configurator",
    ]

    # mixin.multiple_approval attributes
    _approval_from_state = "open"
    _approval_to_state = "done"
    _approval_state = "confirm"
    _after_approved_method = "action_done"

    # Attributes related to add element on view automatically
    _automatically_insert_view_element = True
    _automatically_insert_done_button = False
    _automatically_insert_done_policy_fields = False

    # Attributes related to add element on form view automatically
    _statusbar_visible_label = "draft,ready,open,confirm"
    _policy_field_order = [
        "ready_ok",
        "open_ok",
        "confirm_ok",
        "approve_ok",
        "reject_ok",
        "restart_approval_ok",
        "done_ok",
        "cancel_ok",
        "terminate_ok",
        "restart_ok",
        "manual_number_ok",
    ]
    _header_button_order = [
        "action_ready",
        "action_confirm",
        "action_approve",
        "action_reject",
        "%(ssi_transaction_cancel_mixin.base_select_cancel_reason_action)d",
        "%(ssi_transaction_terminate_mixin.base_select_terminate_reason_action)d",
        "action_restart",
    ]

    # Attributes related to add element on search view automatically
    _state_filter_order = [
        "dom_draft",
        "dom_ready",
        "dom_open",
        "dom_confirm",
        "dom_done",
        "dom_cancel",
        "dom_terminate",
        "dom_reject",
    ]

    # Sequence attribute
    _create_sequence_state = "open"

    date = fields.Date(
        string="Date",
        required=True,
        readonly=True,
        states={"draft": [("readonly", False)]},
        default=lambda r: r._default_date(),
        help="Date of the OKR Objective.",
    )
    project_id = fields.Many2one(
        comodel_name="project.project",
        string="Project",
        required=True,
        readonly=True,
        states={"draft": [("readonly", False)]},
        help="Project related to the OKR Objective.",
    )
    objective = fields.Char(
        string="Objective",
        required=True,
        readonly=True,
        states={"draft": [("readonly", False)]},
        help="Description of the OKR Objective.",
    )
    key_result_ids = fields.One2many(
        comodel_name="okr_key_result",
        inverse_name="objective_id",
        string="Key Results",
        help="Key Results related to the OKR Objective.",
        readonly=True,
    )
    key_result_count = fields.Integer(
        string="Key Result Count",
        compute="_compute_key_result_count",
        help="Number of Key Results related to the OKR Objective.",
        store=True,
        compute_sudo=True,
    )

    @api.model
    def _default_date(self):
        return date.today()

    @api.depends(
        "key_result_ids",
        "key_result_ids.state",
    )
    def _compute_key_result_count(self):
        for record in self:
            valid_key_results = record.key_result_ids.filtered(
                lambda kr: kr.state not in ["cancel", "draft"]
            )
            record.key_result_count = len(valid_key_results)

    # E.11: insert form elements into view
    @ssi_decorator.insert_on_form_view()
    def _insert_form_element(self, view_arch):
        if self._automatically_insert_view_element:
            view_arch = self._reconfigure_statusbar_visible(view_arch)
        return view_arch

    # E.12: provide additional policy fields
    @api.model
    def _get_policy_field(self):
        res = super()._get_policy_field()
        policy_field = [
            "ready_ok",
            "confirm_ok",
            "approve_ok",
            "reject_ok",
            "open_ok",
            "done_ok",
            "cancel_ok",
            "terminate_ok",
            "restart_ok",
            "reject_ok",
            "manual_number_ok",
            "restart_approval_ok",
        ]
        res += policy_field
        return res
