# Approve OKR Key Result

> **Module:** ssi_okr\
> **Model:** `okr_key_result`\
> **Menu:** Project > Key Results\
> **Actor:** active approver on the pending approval level\
> **State:** `confirm` → `done` (automatic once every level is approved)\
> **Requires:** `04-confirm`

## Pre-Condition

- **Record:** Status is **Waiting for Approval**.
- **Config:** An active `policy.template` for `okr_key_result` grants `approve_ok` — the
  standard template does not restrict this to a fixed group; it is granted per record.
- **Access:** User's id is listed in the record's active approvers
  (`active_approver_user_ids`) for the currently pending approval level. When the
  `approval.template` uses sequential approval, only the first unapproved level is
  pending.

## Flow

1. Open the **Project > Key Results** menu.
2. Open the Key Result to approve.
3. Click the **Approve** button.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- If there are still pending approval levels, status remains **Waiting for Approval**
  and the next level becomes pending.
- If all approval levels are fulfilled, the record is automatically moved to **Done** by
  the post-approval action configured on this model — there is no separate Finish button
  for this Key Result.
