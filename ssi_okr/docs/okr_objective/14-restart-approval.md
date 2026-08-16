# Restart Approval Process — OKR Objective

> **Module:** ssi_okr\
> **Model:** `okr_objective`\
> **Menu:** Project > Objectives\
> **Actor:** user in group `Validator` (`okr_objective_validator_group`)\
> **Requires:** `07-start`

## Pre-Condition

- **Record:** Status is **On Progress**.
- **Record:** No `approval.template` is currently assigned to the record
  (`approval_template_id` is empty) — this is normally the case right after **Start**,
  or after the record was moved back to **On Progress** by a `write()` that cleared the
  previously assigned template.
- **Config:** An active `policy.template` for `okr_objective` grants
  `restart_approval_ok` for state `open` to the actor's group, under the condition
  above.
- **Config:** An active `approval.template` for `okr_objective` exists to be matched.
- **Access:** User is in group `Validator` (`okr_objective_validator_group`).

## Flow

1. Open the **Project > Objectives** menu.
2. Open the Objective whose approval process needs to be (re)prepared.
3. Click the **Restart Approval Process** button in the header.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- Any existing approval records for this Objective are removed.
- A matching `approval.template` is (re-)assigned to `approval_template_id`, and new
  approval records are created for each approver level defined by that template —
  without changing the record's status.
