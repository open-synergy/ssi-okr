# Delete OKR Key Result

> **Module:** ssi_okr\
> **Model:** `okr_key_result`\
> **Menu:** Project > Key Results\
> **Actor:** user in group `User` (`okr_key_result_user_group`)\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** Status is **Draft**.
- **Record:** Document number is still **/** (not yet generated — the number is only
  assigned when the Key Result is started).
- **Access:** User is in group `User` (`okr_key_result_user_group`) or `Validator`.

## Flow

1. Open the **Project > Key Results** menu.
2. Select one or more Draft Key Results to delete (check the checkbox).
3. Click **Action** > **Delete**.
4. Click **OK** to confirm.

## Post-Condition

- The selected records are permanently removed from the system.
