# Edit OKR Key Result

> **Module:** ssi_okr\
> **Model:** `okr_key_result`\
> **Menu:** Project > Key Results\
> **Actor:** user in group `User` (`okr_key_result_user_group`)\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** Status is **Draft** — the header fields (**Objective**, **Key Result**,
  **Target Value**, **Unit of Measure**, **Key Result Type**, **Measurement Frequency**,
  **Date**, **Deadline**, **Partner**, **Contact**) are editable, while the
  **Measurements** lines are not.
- **Record:** Status is **On Progress** — only the **Measurements** lines in the
  **Target & Measurement** tab are editable; the header fields become read-only.
- **Access:** User is in group `User` (`okr_key_result_user_group`) or `Validator`.

## Flow

1. Open the **Project > Key Results** menu.
2. Find and open the Key Result to edit.
3. If status is **Draft**, change the required fields (**Objective**, **Key Result**,
   **Target Value**, **Unit of Measure**, **Date**, **Deadline**, **Key Result Type**,
   **Measurement Frequency**) or the optional **Partner** / **Contact** fields.
4. If status is **On Progress**, update the **Measurements** lines in the **Target &
   Measurement** tab. Repeat the following steps as many times as needed:
   - Click **Add a line**.
   - Fill in each line with:
     - **Date** _(required)_: the date the measurement was taken.
     - **User**: automatically filled with the current user. Change if needed.
     - **Value** _(required)_: the measured value.
     - **Assessment** _(required)_: **Green**, **Yellow**, **Red** or **Grey**.
       Automatically filled with **Grey**, which means the Key Result cannot be assessed
       yet (for example it is outside the assessment period). Change it to reflect the
       Key Result at the time of this measurement.
     - **Note**: optional remark.
5. Click **Save**.

## Post-Condition

- The record is updated with the new values.
- If **Measurements** lines were added or changed, **Actual Value** and **Percentage**
  are recomputed from the measurement line with the latest **Date**.
- **Assessment** of the Key Result is recomputed from the **Assessment** of the
  measurement line with the latest **Date**. It falls back to **Grey** when the Key
  Result has no measurement line.
