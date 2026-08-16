// Copyright 2026 OpenSynergy Indonesia
// Copyright 2026 PT. Simetri Sinergi Indonesia
// License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

odoo.define("ssi_okr.okr_objective_tour", function (require) {
    "use strict";

    var tour = require("web_tour.tour");

    // Shared navigation block -- corresponds to Flow 1 of every
    // okr_objective work instruction: "Open the Project > Objectives menu."
    //
    // The rendered menu chain has three clickable levels, not the two the
    // work instruction spells out: the "Project" app (project.menu_main_pm),
    // the second-level "Project" section (ssi_project.menu_project_root_menu)
    // and the "Objectives" leaf. The second level has children but sits at
    // level 2, so it is rendered by Menu.sections as a clickable
    // <a class="dropdown-toggle" data-menu-xmlid> -- only level 3+ menus
    // with children degrade into a non-clickable dropdown header.
    function openObjectiveList() {
        return [
            tour.stepUtils.showAppsMenuItem(),
            {
                content: "Open the Project app",
                trigger: '.o_app[data-menu-xmlid="project.menu_main_pm"]',
            },
            {
                content: "Open the Project menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_project.menu_project_root_menu"]',
            },
            {
                content: "Open the Objectives menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_okr.okr_objective_menu"]',
            },
            {
                // Gate: wait for the TARGET action to be mounted, not just
                // for "some list view" -- opening the app lands on another
                // action first, and that stale list is also a .o_list_view.
                // The landing action can only be "Projects", "Project Phases"
                // or "Project Deliverables", none of which contains
                // "Objectives", so the substring match is unambiguous.
                content: "Objectives list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Objectives)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
        ];
    }

    // Opens the row identified by its Objective column text. Draft records
    // all share the placeholder document number "/", so the Objective text
    // set by setUpClass is the only stable row key.
    function openObjectiveByLabel(objectiveText) {
        return [
            {
                content: "Open the Objective",
                trigger:
                    ".o_data_row:contains(" + objectiveText + ") .o_data_cell:first",
                extra_trigger: ".o_list_view",
            },
            {
                content: "Form is open",
                trigger: ".o_form_view",
                run: function () {
                    // Assertion only.
                },
            },
        ];
    }

    // IK: docs/okr_objective/01-create.md
    tour.register(
        "ssi_okr_okr_objective_create",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            // Flow 1 -- Open the Project > Objectives menu.
            openObjectiveList(),
            [
                // Flow 2 -- Click the Create button.
                {
                    content: "Click Create",
                    trigger: ".o_list_button_add",
                    extra_trigger: ".o_list_view",
                },
                {
                    content: "Form is open in edit mode",
                    trigger: ".o_form_view.o_form_editable",
                    run: function () {
                        // Assertion only.
                    },
                },

                // Flow 3 -- Fill in the required fields. Date is already
                // filled with today's date by its default, and the work
                // instruction only asks to change it "if needed", so it is
                // left as-is here.
                {
                    content: "Fill in the Objective",
                    trigger: ".o_field_widget[name='objective']",
                    extra_trigger: ".o_form_view.o_form_editable",
                    run: "text Tour OKR Objective Create",
                },
                {
                    content: "Fill in Date Start",
                    trigger: ".o_field_widget[name='date_start'] input",
                    extra_trigger: ".o_form_view.o_form_editable",
                    run: "text 01/01/2026",
                },
                {
                    content: "Fill in Date End",
                    trigger: ".o_field_widget[name='date_end'] input",
                    extra_trigger: ".o_form_view.o_form_editable",
                    run: "text 12/31/2026",
                },

                // Flow 4 (Partner and Contact) is explicitly optional and is
                // skipped -- neither field is required to save the record.

                // Flow 5 -- Click Save.
                {
                    content: "Save the record",
                    trigger: ".o_form_button_save",
                },
                {
                    content: "Record is saved",
                    trigger: ".o_form_view.o_form_readonly",
                    run: function () {
                        // Assertion only.
                    },
                },

                // Post-Condition -- a new record is created in Draft status.
                // The second Post-Condition ("the document number still shows
                // /") is a field VALUE and therefore belongs to the unit test,
                // not to this tour.
                {
                    content: "Status is Draft",
                    trigger:
                        ".o_statusbar_status .o_arrow_button[data-value='draft'].btn-primary",
                    run: function () {
                        // Assertion only.
                    },
                },
            ]
        )
    );

    // IK: docs/okr_objective/08-ready.md
    tour.register(
        "ssi_okr_okr_objective_ready",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            // Flow 1 -- Open the Project > Objectives menu.
            openObjectiveList(),
            // Flow 2 -- Open the Objective to stage.
            openObjectiveByLabel("Tour OKR Objective Ready"),
            [
                // Flow 3 -- Click the Stage button.
                {
                    content: "Click the Stage button",
                    trigger: ".o_statusbar_buttons button[name='action_ready']",
                    extra_trigger: ".o_form_view",
                },

                // Flow 4 -- Click OK on the confirmation dialog.
                {
                    content: "Confirm the dialog",
                    trigger: ".modal-footer button.btn-primary",
                    in_modal: true,
                },

                // Post-Condition -- status changes to Ready to Process.
                {
                    content: "Status is Ready to Process",
                    trigger:
                        ".o_statusbar_status .o_arrow_button[data-value='ready'].btn-primary",
                    extra_trigger: "body:not(:has(.modal))",
                    run: function () {
                        // Assertion only.
                    },
                },
            ]
        )
    );

    // IK: docs/okr_objective/07-start.md
    tour.register(
        "ssi_okr_okr_objective_start",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            // Flow 1 -- Open the Project > Objectives menu.
            openObjectiveList(),
            // Flow 2 -- Open the Objective to start.
            openObjectiveByLabel("Tour OKR Objective Start"),
            [
                // Flow 3 -- Click the Start button.
                {
                    content: "Click the Start button",
                    trigger: ".o_statusbar_buttons button[name='action_open']",
                    extra_trigger: ".o_form_view",
                },

                // Flow 4 -- Click OK on the confirmation dialog.
                {
                    content: "Confirm the dialog",
                    trigger: ".modal-footer button.btn-primary",
                    in_modal: true,
                },

                // Post-Condition -- status changes to On Progress. The second
                // Post-Condition ("the document number is assigned from the
                // sequence.template") is a field VALUE and belongs to the unit
                // test, not to this tour.
                {
                    content: "Status is On Progress",
                    trigger:
                        ".o_statusbar_status .o_arrow_button[data-value='open'].btn-primary",
                    extra_trigger: "body:not(:has(.modal))",
                    run: function () {
                        // Assertion only.
                    },
                },
            ]
        )
    );

    // IK: docs/okr_objective/04-confirm.md
    tour.register(
        "ssi_okr_okr_objective_confirm",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            // Flow 1 -- Open the Project > Objectives menu.
            openObjectiveList(),
            // Flow 2 -- Open the Objective to confirm.
            openObjectiveByLabel("Tour OKR Objective Confirm"),
            [
                // Flow 3 -- Click the Confirm button.
                {
                    content: "Click the Confirm button",
                    trigger: ".o_statusbar_buttons button[name='action_confirm']",
                    extra_trigger: ".o_form_view",
                },

                // Flow 4 -- Click OK on the confirmation dialog.
                {
                    content: "Confirm the dialog",
                    trigger: ".modal-footer button.btn-primary",
                    in_modal: true,
                },

                // Post-Condition -- status changes to Waiting for Approval.
                // The approval records created behind it are data, not a
                // user-visible surface, so they are left to the unit test.
                {
                    content: "Status is Waiting for Approval",
                    trigger:
                        ".o_statusbar_status .o_arrow_button[data-value='confirm'].btn-primary",
                    extra_trigger: "body:not(:has(.modal))",
                    run: function () {
                        // Assertion only.
                    },
                },
            ]
        )
    );

    // IK: docs/okr_objective/05-approve.md
    tour.register(
        "ssi_okr_okr_objective_approve",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            // Flow 1 -- Open the Project > Objectives menu.
            openObjectiveList(),
            // Flow 2 -- Open the Objective to approve.
            openObjectiveByLabel("Tour OKR Objective Approve"),
            [
                // Flow 3 -- Click the Approve button.
                {
                    content: "Click the Approve button",
                    trigger:
                        ".o_statusbar_buttons button[name='action_approve_approval']",
                    extra_trigger: ".o_form_view",
                },

                // Flow 4 -- Click OK on the confirmation dialog.
                {
                    content: "Confirm the dialog",
                    trigger: ".modal-footer button.btn-primary",
                    in_modal: true,
                },

                // Post-Condition -- the standard approval.template has a
                // single level, so every level is fulfilled at once and the
                // record moves to Done automatically
                // (_after_approved_method = action_done). There is no
                // separate Finish button for this Objective.
                {
                    content: "Status is Done",
                    trigger:
                        ".o_statusbar_status .o_arrow_button[data-value='done'].btn-primary",
                    extra_trigger: "body:not(:has(.modal))",
                    run: function () {
                        // Assertion only.
                    },
                },
            ]
        )
    );

    // IK: docs/okr_objective/10-cancel.md
    tour.register(
        "ssi_okr_okr_objective_cancel",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            // Flow 1 -- Open the Project > Objectives menu.
            openObjectiveList(),
            // Flow 2 -- Open the Objective to cancel.
            openObjectiveByLabel("Tour OKR Objective Cancel"),
            [
                // Flow 3 -- Click the Cancel button. The button is
                // type="action", so its name= is resolved to a numeric window
                // action id at render time and can never be matched by
                // [name='action_cancel'] -- the label is the only stable
                // handle here.
                {
                    content: "Click the Cancel button",
                    trigger: ".o_statusbar_buttons button:contains(Cancel)",
                    extra_trigger: ".o_form_view",
                },
                {
                    // Wizard gate. In 14.0 an in-modal trigger must NOT be
                    // prefixed with ".modal" -- triggers are already searched
                    // inside the visible modal. Gating on the cancel_reason_id
                    // widget rather than on ".o_form_view" matters: the
                    // record's own form view sits behind the wizard and would
                    // satisfy ".o_form_view" even if the wizard never opened.
                    content: "Wizard is open",
                    trigger: ".o_field_widget[name='cancel_reason_id']",
                    run: function () {
                        // Assertion only.
                    },
                },

                // Flow 4 -- Select the Cancellation Reason. The field is
                // rendered with widget="radio", so it is picked by clicking
                // its label, not by typing into an autocomplete input.
                {
                    content: "Select the cancellation reason",
                    trigger:
                        ".o_field_widget[name='cancel_reason_id'] label:contains(Tour OKR Cancel Reason)",
                },

                // Flow 5 -- Click Confirm.
                {
                    content: "Confirm the wizard",
                    trigger: ".modal-footer button[name='action_confirm']",
                },

                // Flow 6 -- Click OK on the confirmation dialog. The wizard's
                // Confirm button carries confirm="Are you sure?", so this
                // dialog is stacked on top of the wizard.
                {
                    content: "Confirm the stacked dialog",
                    trigger: ".modal-footer button.btn-primary",
                    in_modal: true,
                },

                // Post-Condition -- status changes to Cancelled.
                {
                    content: "Status is Cancelled",
                    trigger:
                        ".o_statusbar_status .o_arrow_button[data-value='cancel'].btn-primary",
                    extra_trigger: "body:not(:has(.modal))",
                    run: function () {
                        // Assertion only.
                    },
                },
            ]
        )
    );
});
