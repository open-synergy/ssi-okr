# Terminate OKR Objective

> **Module:** ssi_okr\
> **Model:** `okr_objective`\
> **Menu:** Project > Objectives\
> **Actor:** user in group `User` (`okr_objective_user_group`)\
> **State:** `open` → `terminate`\
> **Requires:** `07-start`

## Pre-Condition

- **Record:** Status is **On Progress**.
- **Config:** An active `policy.template` for `okr_objective` grants `terminate_ok` for
  state `open` to the actor's group.
- **Access:** User is in group `User` (`okr_objective_user_group`) or `Validator`.

## Flow

1. Open the **Project > Objectives** menu.
2. Open the Objective to terminate.
3. Click the **Terminate** button.
4. In the wizard that appears, select the **Termination Reason**.
5. Click **Confirm**.
6. Click **OK** on the confirmation dialog.

## Post-Condition

- Status changes to **Terminated**.
