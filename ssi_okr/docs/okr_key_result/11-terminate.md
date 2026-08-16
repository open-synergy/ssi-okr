# Terminate OKR Key Result

> **Module:** ssi_okr\
> **Model:** `okr_key_result`\
> **Menu:** Project > Key Results\
> **Actor:** user in group `User` (`okr_key_result_user_group`)\
> **State:** `open` → `terminate`\
> **Requires:** `07-start`

## Pre-Condition

- **Record:** Status is **On Progress**.
- **Config:** An active `policy.template` for `okr_key_result` grants `terminate_ok` for
  state `open` to the actor's group.
- **Access:** User is in group `User` (`okr_key_result_user_group`) or `Validator`.

## Flow

1. Open the **Project > Key Results** menu.
2. Open the Key Result to terminate.
3. Click the **Terminate** button.
4. In the wizard that appears, select the **Termination Reason**.
5. Click **Confirm**.
6. Click **OK** on the confirmation dialog.

## Post-Condition

- Status changes to **Terminated**.
