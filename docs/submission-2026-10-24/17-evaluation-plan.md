# Verification and evaluation plan

The prepared evaluation protocol specifies a single operator and a small controlled example catalogue to check the critical buyer, developer and administrator paths. Functional behaviour is checked against the requirements; AI outputs are compared with a human-defined reference for the same records and inputs.

## Scope and conditions

The planned test set contains six AI requests and six workflow checks. Two request meanings, one matching the stock and one producing no exact match, are expressed equivalently in Russian, Kazakh and English. Each run identifies the application revision, model artifact, browser, hardware and example catalogue. Task timing is recorded where relevant.

## AI selection checks

| Meaning | Expected result | Comparison basis |
| --- | --- | --- |
| A known city, budget and room count that match the example catalogue. | Returned IDs exist, are public and Available, and meet the stated conditions; the reply language matches the request. | Manual filtering of the same records against the written constraints. |
| Conditions producing no exact match. | Explain that no exact result exists, propose a specific change and obtain confirmation before relaxing it. | Manual confirmation of the empty exact-match set and review of the proposed condition change. |

Each request is assessed using its extracted preferences, returned records and explanation together. Its result records pass/fail and the reason for any mismatch. The six cases provide a focused demonstration of the specified behaviours.

## End-to-end checks

| Check | Demonstration path and expected behaviour | Main requirement coverage |
| --- | --- | --- |
| DEMO-01 Buyer selection and enquiry | The catalogue -> development -> floor -> apartment path retains the selected unit. Plan and base price are visible, comparison and favourites respect their access rules, and the accepted enquiry reaches the owning developer. | FR-01/02, FR-05 through FR-14, FR-33/34 |
| DEMO-02 Draft and first publication | A saved private draft can be reopened. Publication identifies missing mandatory data and becomes available after completion. Extra finishing, photos, 3D and panoramas are optional. A later valid save updates public content immediately. | FR-15 through FR-20 |
| DEMO-03 Commercial state | Changes made after an enquiry form opens trigger confirmation of a new price, reselection of a removed offer or rejection of unavailable stock. An accepted enquiry retains its submitted snapshot. | FR-11/12, FR-33 |
| DEMO-04 Access and moderation | Ownership checks prevent unrelated access. Hiding requires an owner-visible reason and restricts public entry points. Company reactivation preserves separate development restrictions and private drafts. | FR-04, FR-36/37, NFR-01 |
| DEMO-05 Region correction | One facade and one floor-plan input produce separate candidate records. The corrected geometry and record links are compared with manual preparation on the same input. | FR-07/08, FR-27/28 |
| DEMO-06 Enquiry and supporting functions | Enquiry status changes in the owning inbox appear in buyer history. Audit entries and reference protection match the specified rules. Supplied map and viewer content opens through the relevant property context. | FR-29 through FR-32, FR-34/35, FR-39/40 |

The requirement matrix supplies the detailed checklist within each workflow. Particular attention is given to ownership, public visibility, physical-apartment identity and confirmed-price handling.

## Region quality and correction effort

Facade-floor suggestions and floor-plan apartment suggestions have separate comparisons with manually prepared references. The assessment records missing, extra or fragmented regions, geometry changes, final record-link correctness and the correction effort needed for a usable result.

Preparation-time comparisons include inference, waiting, correction and record assignment on the same input. Both paths are assessed at comparable final geometry and link quality. The resulting case records describe the tested inputs and conditions.

## Result record

| Field | Recorded content |
| --- | --- |
| Case and version | Scenario ID, date, application/model revision and browser/hardware. |
| Expected | Required output or access, visibility and commercial rule. |
| Observed | Actual behaviour and pass/fail outcome. |
| Evidence | Screenshot, returned IDs, saved enquiry or task recording, with personal details redacted. |
| Follow-up | Defect, responsible member, correction and retest reference. |

Results are assessed per case and linked to the relevant requirement and project revision. The team summarises successful paths, defects, corrections and the practical limits of the demonstration.
