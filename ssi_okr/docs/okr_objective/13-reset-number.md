# Reset Document Number — OKR Objective

> **Module:** ssi_okr\
> **Model:** `okr_objective`\
> **Menu:** Project > Objectives\
> **Actor:** user in group `Validator` (`okr_objective_validator_group`)\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** Status is **Draft**.
- **Config:** An active `sequence.template` exists for `okr_objective`.
- **Access:** User is in group `Validator` (`okr_objective_validator_group`).

## Flow

1. Open the **Project > Objectives** menu.
2. Open the Draft Objective whose document number will be reset.
3. Click the **Reset Document Number** button (or edit the **Name** field and change it
   to **/**).
4. Click **OK** on the confirmation dialog (only when the button was used).

## Post-Condition

- Document number returns to **/**.
- The record will receive an automatic number when it transitions to **On Progress**
  (see `07-start`), according to the `sequence.template` configuration.
