# Delete OKR Objective

> **Module:** ssi_okr\
> **Model:** `okr_objective`\
> **Menu:** Project > Objectives\
> **Actor:** user in group `User` (`okr_objective_user_group`)\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** Status is **Draft**.
- **Record:** Document number is still **/** (not yet generated — the number is only
  assigned when the Objective is started).
- **Access:** User is in group `User` (`okr_objective_user_group`) or `Validator`.

## Flow

1. Open the **Project > Objectives** menu.
2. Select one or more Draft Objectives to delete (check the checkbox).
3. Click **Action** > **Delete**.
4. Click **OK** to confirm.

## Post-Condition

- The selected records are permanently removed from the system.
