# Create OKR Objective

> **Module:** ssi_okr\
> **Model:** `okr_objective`\
> **Menu:** Project > Objectives\
> **Actor:** user in group `User` (`okr_objective_user_group`)\
> **State:** `—` → `draft`

## Pre-Condition

- **Data:** None required beforehand — `partner_id` and `contact_partner_id` are
  optional on creation.
- **Access:** User is in group `User` (`okr_objective_user_group`) or the higher
  `Validator` group, which includes it.

## Flow

1. Open the **Project > Objectives** menu.
2. Click the **Create** button.
3. Fill in the required fields:
   - **Date**: automatically filled with today's date. Change if needed.
   - **Objective**: the goal statement for this OKR cycle.
   - **Date Start** and **Date End**: the duration covered by this Objective.
4. Optionally set **Partner** and **Contact** to associate the Objective with a partner.
5. Click **Save**.

## Post-Condition

- A new record is created in **Draft** status.
- The document number (**Name**) still shows **/** — it is only assigned when the
  Objective is started (see `07-start`).

## Related Views

- The **Key Results** smart button on the button box (`action_open_key_result`) is pure
  navigation — it opens the list of `okr_key_result` records linked to this Objective
  and does not write any field or change status. It carries no IK of its own.
