# Copyright 2025 OpenSynergy Indonesia
# Copyright 2025 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from datetime import date

from odoo import api, fields, models

from odoo.addons.ssi_decorator import ssi_decorator


class OkrKeyResult(models.Model):
    _name = "okr_key_result"
    _description = "OKR Key Result"
    _inherit = [
        "mixin.transaction_terminate",
        "mixin.transaction_cancel",
        "mixin.transaction_done",
        "mixin.transaction_confirm",
        "mixin.transaction_open",
        "mixin.transaction_ready",
        "mixin.transaction_partner",
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
        help="Date of the OKR Key Result.",
    )
    partner_id = fields.Many2one(
        required=False,
    )
    objective_id = fields.Many2one(
        comodel_name="okr_objective",
        string="Objective",
        required=True,
        readonly=True,
        states={"draft": [("readonly", False)]},
        help="Objective related to the OKR Key Result.",
    )
    date_deadline = fields.Date(
        string="Deadline",
        required=True,
        readonly=True,
        states={"draft": [("readonly", False)]},
        help="Deadline of the OKR Key Result.",
    )
    key_result = fields.Char(
        string="Key Result",
        required=True,
        readonly=True,
        states={"draft": [("readonly", False)]},
        help="Description of the OKR Key Result.",
    )
    target_value = fields.Float(
        string="Target Value",
        required=True,
        readonly=True,
        states={"draft": [("readonly", False)]},
        help="Target value of the OKR Key Result.",
    )
    measurement_ids = fields.One2many(
        comodel_name="okr_key_result.measurement",
        inverse_name="key_result_id",
        string="Measurements",
        help="Measurements of the OKR Key Result.",
        readonly=True,
        states={"open": [("readonly", False)]},
    )
    actual_value = fields.Float(
        string="Actual Value",
        compute="_compute_actual_value",
        help="Actual value of the OKR Key Result.",
        store=True,
        compute_sudo=True,
    )
    uom_id = fields.Many2one(
        comodel_name="uom.uom",
        string="Unit of Measure",
        required=True,
        readonly=True,
        states={"draft": [("readonly", False)]},
        help="Unit of measure of the OKR Key Result.",
    )
    percentage = fields.Float(
        string="Percentage",
        compute="_compute_percentage",
        help="Percentage of the OKR Key Result.",
        store=True,
        compute_sudo=True,
    )

    deliverable_ids = fields.Many2many(
        comodel_name="project_deliverable",
        string="Deliverables",
        help="Deliverables related to the OKR Key Result.",
        relation="rel_okr_key_result_2_deliverable",
        column1="okr_key_result_id",
        column2="deliverable_id",
    )
    deliverable_count = fields.Integer(
        string="Deliverable Count",
        compute="_compute_deliverable",
        store=True,
        compute_sudo=True,
    )
    open_deliverable_count = fields.Integer(
        string="On-Going Deliverable Count",
        compute="_compute_deliverable",
        store=True,
        compute_sudo=True,
    )
    completed_deliverable_count = fields.Integer(
        string="Completed Deliverable Count",
        compute="_compute_deliverable",
        store=True,
        compute_sudo=True,
    )
    cancelled_deliverable_count = fields.Integer(
        string="Cancelled Deliverable Count",
        compute="_compute_deliverable",
        store=True,
        compute_sudo=True,
    )
    terminated_deliverable_count = fields.Integer(
        string="Terminated Deliverable Count",
        compute="_compute_deliverable",
        store=True,
        compute_sudo=True,
    )
    percentage_deliverable_completed = fields.Float(
        string="Percentage of Completed Deliverable",
        compute="_compute_deliverable",
        store=True,
        compute_sudo=True,
    )
    percentage_deliverable_open = fields.Float(
        string="Percentage of On-Going Deliverable",
        compute="_compute_deliverable",
        store=True,
        compute_sudo=True,
    )
    percentage_deliverable_cancelled = fields.Float(
        string="Percentage of Cancelled Deliverable",
        compute="_compute_deliverable",
        store=True,
        compute_sudo=True,
    )
    percentage_deliverable_terminated = fields.Float(
        string="Percentage of Terminated Deliverable",
        compute="_compute_deliverable",
        store=True,
        compute_sudo=True,
    )

    @api.depends("deliverable_ids", "deliverable_ids.state")
    def _compute_deliverable(self):
        for record in self:
            deliverables = record.deliverable_ids
            record.deliverable_count = len(deliverables)
            if deliverables:
                open_deliverables = deliverables.filtered(
                    lambda d: d.state in ["draft", "ready", "open", "confirm"]
                )
                completed_deliverables = deliverables.filtered(
                    lambda d: d.state == "done"
                )
                cancelled_deliverables = deliverables.filtered(
                    lambda d: d.state == "cancel"
                )
                terminated_deliverables = deliverables.filtered(
                    lambda d: d.state == "terminate"
                )
                record.open_deliverable_count = len(open_deliverables)
                record.completed_deliverable_count = len(completed_deliverables)
                record.cancelled_deliverable_count = len(cancelled_deliverables)
                record.terminated_deliverable_count = len(terminated_deliverables)
                record.percentage_deliverable_completed = len(
                    completed_deliverables
                ) / len(deliverables)
                record.percentage_deliverable_open = len(open_deliverables) / len(
                    deliverables
                )
                record.percentage_deliverable_cancelled = len(
                    cancelled_deliverables
                ) / len(deliverables)
                record.percentage_deliverable_terminated = len(
                    terminated_deliverables
                ) / len(deliverables)
            else:
                record.open_deliverable_count = 0
                record.completed_deliverable_count = 0
                record.cancelled_deliverable_count = 0
                record.terminated_deliverable_count = 0
                record.percentage_deliverable_completed = 0.0
                record.percentage_deliverable_open = 0.0
                record.percentage_deliverable_cancelled = 0.0
                record.percentage_deliverable_terminated = 0.0

    @api.depends(
        "target_value",
        "measurement_ids.value",
        "measurement_ids.date",
        "measurement_ids",
    )
    def _compute_actual_value(self):
        for record in self:
            record.percentage = 0.0
            # Loop measurement_ids to get the latest measurement value
            if record.measurement_ids:
                latest_measurement = max(
                    record.measurement_ids, key=lambda m: m.date or date.min
                )
                record.actual_value = latest_measurement.value

    @api.depends(
        "target_value",
        "measurement_ids.value",
        "measurement_ids.date",
        "measurement_ids",
    )
    def _compute_percentage(self):
        for record in self:
            if record.target_value:
                record.percentage = record.actual_value / record.target_value
            else:
                record.percentage = 0.0

    @api.model
    def _default_date(self):
        return date.today()

    @api.onchange(
        "partner_id",
    )
    def onchange_objective_id(self):
        self.objective_id = False

    @api.onchange(
        "objective_id",
    )
    def onchange_date_deadline(self):
        self.date_deadline = False
        if self.objective_id and self.objective_id.date_end:
            self.date_deadline = self.objective_id.date_end

    def action_open_deliverable(self):
        self.ensure_one()
        action = self.env.ref("ssi_project.project_deliverable_action").read()[0]
        action["domain"] = [("id", "in", self.deliverable_ids.ids)]
        return action

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
            "confirm_ok",
            "ready_ok",
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
