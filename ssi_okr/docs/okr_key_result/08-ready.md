# Stage OKR Key Result

> **Module:** ssi_okr\
> **Model:** `okr_key_result`\
> **Menu:** Project > Key Results\
> **Actor:** user in group `User` (`okr_key_result_user_group`)\
> **State:** `draft` → `ready`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** Status is **Draft**.
- **Config:** An active `policy.template` for `okr_key_result` grants `ready_ok` for
  state `draft` to the actor's group.
- **Access:** User is in group `User` (`okr_key_result_user_group`) or `Validator`.

## Flow

1. Open the **Project > Key Results** menu.
2. Open the Key Result to stage.
3. Click the **Stage** button.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- Status changes to **Ready to Process**.
