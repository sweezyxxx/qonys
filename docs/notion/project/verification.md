# Verification Scenarios

Verification checks implemented behaviour against [[requirements]]. The initial profile is a single operator using a controlled catalogue, with the application revision, browser, hardware and model artifacts identified for the run. Design-prototype inspection and application/AI evaluation are recorded as different kinds of evidence.

## Workflow checks

| Case | Path and expected behaviour | Coverage |
| --- | --- | --- |
| V-01 Buyer path | Catalogue → development → floor → apartment resolves the intended physical record; comparison and enquiry retain offer context and access gates | FR-01/02, FR-05–FR-14, FR-33/34 |
| V-02 Private draft and release | Incomplete content survives reopening; publication reports exact blockers; completing required data enables first release without optional extras | FR-15–FR-20 |
| V-03 Commercial changes | Price changes require confirmation; removed offers require replacement; unavailable stock rejects new enquiry; accepted snapshots remain historical | FR-10–FR-12, FR-33 |
| V-04 Ownership and restrictions | Unrelated access fails; hiding has an owner-visible reason; company reactivation preserves individual hides and private drafts | FR-04, FR-36/37, NFR-01 |
| V-05 Region preparation | Facade and floor-plan candidates are corrected and linked to their intended records; manual preparation remains possible | FR-07/08, FR-21, FR-27/28 |
| V-06 Supporting workflows | Inbox/status/history, SMTP failure, reference protection, audit/counts, map and supplied optional viewers follow the specification | FR-29–FR-40, NFR-05 |

Detailed acceptance also covers the three languages, mobile layouts, confidential outputs, dependency reproducibility and data integrity. Required rejection paths include a cross-company identifier, a hidden direct file, unverified buyer action, wrong-floor mapping and a referenced-value deletion.

## Buyer AI cases

Two request meanings are expressed equivalently in Russian, Kazakh and English, giving six initial cases. One meaning matches the stock; the other produces no exact match. Each case checks extracted fields, actual returned IDs, hard constraints, known-fact explanations, reply language and confirmation before relaxation.

Manual filtering of the same catalogue is the comparison baseline. A valid response format alone is not a pass. The six cases demonstrate the tested behaviours without establishing broad multilingual accuracy.

## Image preparation comparison

Facade-floor and floor-plan apartment suggestions are assessed separately against manually prepared references. Records cover missing/extra/fragmented regions, corrections, final geometry and correct catalogue links. Any time comparison includes inference, waiting, correction and assignment at comparable final quality.

## Result record

Each result identifies its case and requirement, date, application/model revision, browser/hardware, input data, expected and observed behaviour, pass/fail, evidence and any defect/correction/retest. A plan is not entered as a successful run. Meaningful failures remain traceable to the issue and revision that resolves them.

The milestone's local HTML inspection is retained in [[defence-prototype]]. Its results concern that design artifact and do not stand in for integrated backend or AI tests. [[delivery]] defines review and task traceability.
