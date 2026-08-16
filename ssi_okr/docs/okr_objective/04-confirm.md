# Confirm OKR Objective

> **Module:** ssi_okr\
> **Model:** `okr_objective`\
> **Menu:** Project > Objectives\
> **Actor:** user in group `User` (`okr_objective_user_group`)\
> **State:** `open` → `confirm`\
> **Requires:** `07-start`

## Pre-Condition

- **Record:** Status is **On Progress**.
- **Config:** An active `policy.template` for `okr_objective` grants `confirm_ok` for
  state `open` to the actor's group.
- **Config:** An active `approval.template` for `okr_objective` matches this record and
  has at least one approver level (the standard template routes approval to group
  `Validator`).
- **Access:** User is in group `User` (`okr_objective_user_group`) or `Validator`.

## Flow

1. Open the **Project > Objectives** menu.
2. Open the Objective to confirm.
3. Click the **Confirm** button.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- Status changes to **Waiting for Approval**.
- Approval records are created for each approver level defined by the matched
  `approval.template`.
