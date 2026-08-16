// Copyright 2026 OpenSynergy Indonesia
// Copyright 2026 PT. Simetri Sinergi Indonesia
// License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

odoo.define("ssi_okr.okr_key_result_tour", function (require) {
    "use strict";

    var tour = require("web_tour.tour");

    // Shared navigation block -- corresponds to Flow 1 of every
    // okr_key_result work instruction: "Open the Project > Key Results
    // menu."
    //
    // The rendered menu chain has three clickable levels, not the two the
    // work instruction spells out: the "Project" app (project.menu_main_pm),
    // the second-level "Project" section (ssi_project.menu_project_root_menu)
    // and the "Key Results" leaf. The second level has children but sits at
    // level 2, so it is rendered by Menu.sections as a clickable
    // <a class="dropdown-toggle" data-menu-xmlid> -- only level 3+ menus
    // with children degrade into a non-clickable dropdown header.
    function openKeyResultList() {
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
                content: "Open the Key Results menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_okr.okr_key_result_menu"]',
            },
            {
                // Gate: wait for the TARGET action to be mounted, not just
                // for "some list view" -- opening the app lands on another
                // action first, and that stale list is also a .o_list_view.
                // The landing action can only be "Projects", "Project Phases"
                // or "Project Deliverables", none of which contains
                // "Key Results", so the substring match is unambiguous.
                content: "Key Results list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Key Results)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
        ];
    }

    // Opens the row identified by its Key Result column text. Draft records
    // all share the placeholder document number "/", so the Key Result text
    // set by setUpClass is the only stable row key.
    function openKeyResultByLabel(keyResultText) {
        return [
            {
                content: "Open the Key Result",
                trigger:
                    ".o_data_row:contains(" + keyResultText + ") .o_data_cell:first",
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

    // IK: docs/okr_key_result/01-create.md
    tour.register(
        "ssi_okr_okr_key_result_create",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            // Flow 1 -- Open the Project > Key Results menu.
            openKeyResultList(),
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

                // Flow 3 (Partner) is explicitly optional and is skipped --
                // leaving it empty keeps the Objective domain at
                // [('partner_id', '=', False)], which the fixture Objective
                // satisfies.

                // Flow 4 -- Fill in the required fields. The fixture
                // Objective carries a manually assigned document number,
                // because a Draft transaction's name_get() returns "*<id>"
                // and could not be typed into the autocomplete otherwise.
                {
                    content: "Type the Objective",
                    trigger: ".o_field_many2one[name='objective_id'] input",
                    extra_trigger: ".o_form_view.o_form_editable",
                    run: "text TOUR-OKR-OBJ",
                },
                {
                    content: "Pick the Objective from the dropdown",
                    trigger: ".ui-autocomplete .ui-menu-item a:contains(TOUR-OKR-OBJ)",
                    in_modal: false,
                },
                {
                    content: "Fill in the Key Result",
                    trigger: ".o_field_widget[name='key_result']",
                    extra_trigger: ".o_form_view.o_form_editable",
                    run: "text Tour OKR Key Result Create",
                },
                {
                    content: "Fill in the Target Value",
                    trigger: ".o_field_widget[name='target_value']",
                    extra_trigger: ".o_form_view.o_form_editable",
                    run: "text 100",
                },
                {
                    content: "Type the Unit of Measure",
                    trigger: ".o_field_many2one[name='uom_id'] input",
                    extra_trigger: ".o_form_view.o_form_editable",
                    run: "text Tour OKR KR Unit",
                },
                {
                    content: "Pick the Unit of Measure from the dropdown",
                    trigger:
                        ".ui-autocomplete .ui-menu-item a:contains(Tour OKR KR Unit)",
                    in_modal: false,
                },

                // Date is already filled with today's date by its default and
                // Deadline is filled from the Objective's end date by the
                // onchange, and the work instruction only asks to change them
                // "if needed", so both are left as-is here.

                // Flow 5 (Contact) is explicitly optional and is skipped.

                // Flow 6 -- Click Save.
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
                // The other two Post-Conditions (the document number still
                // shows /, and the Measurements lines are not editable yet)
                // are field VALUES and therefore belong to the unit test, not
                // to this tour.
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

    // IK: docs/okr_key_result/08-ready.md
    tour.register(
        "ssi_okr_okr_key_result_ready",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            // Flow 1 -- Open the Project > Key Results menu.
            openKeyResultList(),
            // Flow 2 -- Open the Key Result to stage.
            openKeyResultByLabel("Tour OKR Key Result Ready"),
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

    // IK: docs/okr_key_result/07-start.md
    tour.register(
        "ssi_okr_okr_key_result_start",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            // Flow 1 -- Open the Project > Key Results menu.
            openKeyResultList(),
            // Flow 2 -- Open the Key Result to start.
            openKeyResultByLabel("Tour OKR Key Result Start"),
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

                // Post-Condition -- status changes to On Progress. The other
                // two Post-Conditions (the document number assigned from the
                // sequence.template, and the Measurements lines becoming
                // editable) are field VALUES and belong to the unit test, not
                // to this tour.
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

    // IK: docs/okr_key_result/04-confirm.md
    tour.register(
        "ssi_okr_okr_key_result_confirm",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            // Flow 1 -- Open the Project > Key Results menu.
            openKeyResultList(),
            // Flow 2 -- Open the Key Result to confirm.
            openKeyResultByLabel("Tour OKR Key Result Confirm"),
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

    // IK: docs/okr_key_result/05-approve.md
    tour.register(
        "ssi_okr_okr_key_result_approve",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            // Flow 1 -- Open the Project > Key Results menu.
            openKeyResultList(),
            // Flow 2 -- Open the Key Result to approve.
            openKeyResultByLabel("Tour OKR Key Result Approve"),
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
                // separate Finish button for this Key Result.
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

    // IK: docs/okr_key_result/10-cancel.md
    tour.register(
        "ssi_okr_okr_key_result_cancel",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            // Flow 1 -- Open the Project > Key Results menu.
            openKeyResultList(),
            // Flow 2 -- Open the Key Result to cancel.
            openKeyResultByLabel("Tour OKR Key Result Cancel"),
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
                        ".o_field_widget[name='cancel_reason_id'] label:contains(Tour OKR KR Cancel Reason)",
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
