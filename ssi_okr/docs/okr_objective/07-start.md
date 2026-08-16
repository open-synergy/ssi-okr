# Start OKR Objective

> **Module:** ssi_okr\
> **Model:** `okr_objective`\
> **Menu:** Project > Objectives\
> **Actor:** user in group `User` (`okr_objective_user_group`)\
> **State:** `ready` → `open`\
> **Requires:** `08-ready`

## Pre-Condition

- **Record:** Status is **Ready to Process**.
- **Config:** An active `policy.template` for `okr_objective` grants `open_ok` for state
  `ready` to the actor's group.
- **Config:** An active `sequence.template` exists for `okr_objective` — the document
  number is generated at this transition.
- **Access:** User is in group `User` (`okr_objective_user_group`) or `Validator`.

## Flow

1. Open the **Project > Objectives** menu.
2. Open the Objective to start.
3. Click the **Start** button.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- Status changes to **On Progress**.
- The document number (**Name**) is assigned from the `sequence.template` configured for
  this model, replacing the placeholder **/**.
