# Application Contracts

These logical contracts define the responsibilities shared by Flutter Web, Django and workers. Operation names and example fields express the design boundary; concrete routes and serialisation are maintained with the implementation API schema. Domain acceptance remains defined by [[requirements]] and [[states]].

## Operation responsibilities

| Operation | Input context | Successful result | Relevant rejection or clarification |
| --- | --- | --- | --- |
| Read city catalogue | Selected city and discovery context | Eligible development cards/markers | Restricted developments excluded consistently. |
| Read development/floor | Development, building and floor identifiers | Correct public content, plan and reviewed links | Non-public content protected; cross-parent links rejected. |
| Read apartment offer | Physical apartment and optional explicit finishing | Characteristics, status, base/selected offer and current price | Removed offer requires a valid selection; hidden development protected. |
| Save owned development section | Caller, owned object and changed section | Persisted private data or valid immediate public update | Ownership, field, translation or mapping errors. |
| Validate/publish development | Owned development | Blockers by editing section, or completed first publication | Missing mandatory data and administrative restriction. |
| Prepare image candidates | Owned image, task type and object context | Trackable job and candidate output | Invalid ownership/input or processing failure. |
| Save reviewed regions | Source image, edited geometry and target links | Reviewed valid associations | Wrong company/building/floor or invalid mapping. |
| Interpret/search buyer preferences | Message language, conversation context and conditions | Clarification, exact matches or a specific proposed relaxation | Unsupported values, ambiguity or no exact matches. |
| Accept enquiry | Verified buyer, object/offer, contact and displayed price | Accepted enquiry identity and submitted snapshot | Verification, visibility, availability, price or selected-offer change. |
| Process/archive enquiry | Owning company, enquiry and processing operation | Updated processing view and buyer history | Unrelated company or invalid operation context. |
| Moderate development/company | Administrator, target and required reason | Restricted/restored state with key audit event | Missing reason, unauthorised actor or invalid target. |

## Apartment and offer context

An apartment identifier always selects the physical unit. An additional offer identifier is optional: its absence means the base condition and base price, not a missing apartment offer. Client comparisons and assistant results carry an explicit offer only when one was selected.

Illustrative enquiry intent:

```json
{
  "apartment_id": "example-apartment-34",
  "additional_finishing_id": null,
  "displayed_price": 3607000,
  "contact": {
    "name": "Example",
    "surname": "Buyer",
    "phone": "example contact"
  },
  "comment": "Please contact me about this apartment."
}
```

Identifiers and values above are illustrative. The backend resolves owner, visibility, availability and current commercial context. It does not accept client-supplied company ownership or a stale displayed price as domain truth.

## Changed-price response

If the price has changed, the client shows the current offer and obtains confirmation. Acceptance rechecks that confirmed state when saving; repeated changes cannot be hidden by a previous confirmation. If the selected extra offer was removed, a replacement is selected before acceptance. If availability or visibility changed, a new enquiry is not accepted.

## Validation results

Field issues identify the relevant field; publication issues also identify its editing section. Processing results distinguish job progress/failure from valid domain output. AI results distinguish clarification, exact matches and a relaxation proposal, so the client does not display an unconfirmed relaxed search as an exact result.

[[jobs]] owns asynchronous execution and file handling. [[roles]] owns caller boundaries. [[enquiries]] owns durable acceptance and notifications.
