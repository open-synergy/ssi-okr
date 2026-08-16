# Start OKR Key Result

> **Module:** ssi_okr\
> **Model:** `okr_key_result`\
> **Menu:** Project > Key Results\
> **Actor:** user in group `User` (`okr_key_result_user_group`)\
> **State:** `ready` → `open`\
> **Requires:** `08-ready`

## Pre-Condition

- **Record:** Status is **Ready to Process**.
- **Config:** An active `policy.template` for `okr_key_result` grants `open_ok` for
  state `ready` to the actor's group.
- **Config:** An active `sequence.template` exists for `okr_key_result` — the document
  number is generated at this transition.
- **Access:** User is in group `User` (`okr_key_result_user_group`) or `Validator`.

## Flow

1. Open the **Project > Key Results** menu.
2. Open the Key Result to start.
3. Click the **Start** button.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- Status changes to **On Progress**.
- The document number (**Name**) is assigned from the `sequence.template` configured for
  this model, replacing the placeholder **/**.
- The **Measurements** lines in the **Target & Measurement** tab become editable (see
  `02-edit`).
