# Create OKR Key Result

> **Module:** ssi_okr\
> **Model:** `okr_key_result`\
> **Menu:** Project > Key Results\
> **Actor:** user in group `User` (`okr_key_result_user_group`)\
> **State:** `—` → `draft`

## Pre-Condition

- **Record:** An `okr_objective` record exists to serve as the parent — the
  **Objective** field is filtered by matching **Partner**, so at least one Objective
  with a matching (or empty) **Partner** must exist.
- **Data:** None required beforehand besides the parent Objective — **Partner** and
  **Contact** are optional on creation.
- **Access:** User is in group `User` (`okr_key_result_user_group`) or the higher
  `Validator` group, which includes it.

## Flow

1. Open the **Project > Key Results** menu.
2. Click the **Create** button.
3. Optionally set **Partner** to associate the Key Result with a partner — this filters
   the **Objective** field below to Objectives sharing the same **Partner**.
4. Fill in the required fields:
   - **Objective** _(required)_: select the parent OKR Objective this Key Result belongs
     to.
   - **Key Result** _(required)_: description of this Key Result.
   - **Target Value** _(required)_: the numeric target to reach.
   - **Unit of Measure** _(required)_: the unit **Target Value** and **Actual Value**
     are measured in.
   - **Date**: automatically filled with today's date. Change if needed.
   - **Deadline**: automatically filled from **Objective**'s end date if set. Change if
     needed.
5. Optionally set **Contact** to associate the Key Result with a specific contact of the
   selected **Partner**.
6. Click **Save**.

## Post-Condition

- A new record is created in **Draft** status.
- The document number (**Name**) still shows **/** — it is only assigned when the Key
  Result is started (see `07-start`).
- The **Measurements** lines in the **Target & Measurement** tab cannot be added yet —
  they only become editable once the record is **On Progress** (see `02-edit`).

## Related Views

- The **Deliverables** smart button on the button box (`action_open_deliverable`) is
  pure navigation — it opens the list of `project_deliverable` records linked through
  `deliverable_ids` and does not write any field or change status. It carries no IK of
  its own.
