# Cancel OKR Key Result

> **Module:** ssi_okr\
> **Model:** `okr_key_result`\
> **Menu:** Project > Key Results\
> **Actor:** user in group `Validator` (`okr_key_result_validator_group`)\
> **State:** `draft` | `ready` | `open` | `done` | `terminate` → `cancel`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** Status is **Draft**, **Ready to Process**, **On Progress**, **Done**, or
  **Terminated**.
- **Config:** An active `policy.template` for `okr_key_result` grants `cancel_ok` for
  that state to the actor's group.
- **Access:** User is in group `Validator` (`okr_key_result_validator_group`).

## Flow

1. Open the **Project > Key Results** menu.
2. Open the Key Result to cancel.
3. Click the **Cancel** button.
4. In the wizard that appears, select the **Cancellation Reason**.
5. Click **Confirm**.
6. Click **OK** on the confirmation dialog.

## Post-Condition

- Status changes to **Cancelled**.
