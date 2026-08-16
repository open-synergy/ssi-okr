# Stage OKR Objective

> **Module:** ssi_okr\
> **Model:** `okr_objective`\
> **Menu:** Project > Objectives\
> **Actor:** user in group `User` (`okr_objective_user_group`)\
> **State:** `draft` → `ready`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** Status is **Draft**.
- **Config:** An active `policy.template` for `okr_objective` grants `ready_ok` for
  state `draft` to the actor's group.
- **Access:** User is in group `User` (`okr_objective_user_group`) or `Validator`.

## Flow

1. Open the **Project > Objectives** menu.
2. Open the Objective to stage.
3. Click the **Stage** button.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- Status changes to **Ready to Process**.
