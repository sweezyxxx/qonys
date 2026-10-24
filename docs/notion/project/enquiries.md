# Enquiries and Notifications

An enquiry lets a verified buyer contact the owning developer about a specific apartment/finishing offer or available parking place. It preserves commercial context and processing history; it does not purchase, pay for or reserve the object.

Requirements: FR-14, FR-30 and FR-33–FR-35, with NFR-05. See [[requirements]].

## Submission

The form collects name, surname, phone and an optional comment. Saved buyer details are prefilled and remain correctable. The selected object and offer are attached automatically. Public manager telephone numbers are not displayed.

Before acceptance, the backend checks verified buyer identity, development visibility, object ownership, availability, selected offer and current price. The client presentation is not the authority for these facts.

| Change since opening the form | Required outcome |
| --- | --- |
| Price changed | Show the current price and obtain buyer confirmation before acceptance. |
| Selected extra offer removed | Require a valid replacement; the base apartment remains usable without extra offers. |
| Apartment/parking became unavailable | Reject a new enquiry and show the current status. |
| Development became restricted | Protect the content and prevent a new public enquiry. |
| Contact form incomplete or invalid | Return the relevant validation issue without accepting the enquiry. |

Acceptance saves buyer contact data, selected object/offer and the confirmed submitted-price snapshot. Later stock or price edits do not rewrite that snapshot. A corrected enquiry contact does not imply an automatic profile change.

## Developer and buyer views

The enquiry appears in the owning company inbox and the buyer's My enquiries history. The developer processes it through New, In progress, Processed and Cancelled. These processing states do not change apartment/parking availability.

Completed enquiries can be archived and reopened for viewing. Permanent developer deletion is excluded. Buyer history shows the object, submission date and current processing state.

## SMTP notification

The accepted inbox record is durable independently of SMTP delivery. A background notification attempt can fail without deleting the record or requiring the buyer to recreate an already accepted enquiry. Delivery recovery refers to the same enquiry and snapshot.

In-account written dialogue, preferred contact channels and automatic reservations are outside the current baseline. Interview requests for them remain recorded in [[defence]].

Acceptance includes correct inbox ownership, changed-price confirmation, removed-offer handling, unavailable-stock rejection, snapshot preservation, status/history consistency and mail-failure durability. See [[contracts]], [[jobs]] and [[states]].
