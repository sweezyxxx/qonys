# Key scenario design prototype

An interactive [QONYS prototype](prototype/index.html) was prepared for the analysis and design milestone. It runs locally in a browser without a server. Its scenario strip provides access to the buyer, developer and administrator examples for design review.

The prototype uses fictional developments, plans, prices and accounts to demonstrate screen transitions and business rules. Reloading restores the example state. The screens are in English, and the developer form represents the three stored language versions. The application architecture specifies Flutter Web and the Django API; this HTML artifact documents the intended interaction.

## Buyer scenario

The buyer flow connects the catalogue, Demo Court development, floor 5 and apartment 34. The apartment screen combines the supplied plan, characteristics and current price. Its compact finishing dropdown changes the full price and description while retaining the same physical apartment.

The comparison records the selected apartment and finishing. The enquiry path displays a sign-in gate for a guest; the example verified-buyer transition preserves comparison entries. The enquiry form carries the apartment, finishing and price automatically, and its local submission creates a snapshot for the developer inbox.

The floor example uses translucent yellow and red for Reserved and Sold units and disables selection of those units. Optional sections follow content availability. The assistant displays a labelled example response to illustrate the proposed conversation and result presentation.

## Developer scenario

The floor-plan editor represents position adjustment, apartment assignment and explicit confirmation of a candidate region. The scenario covers correction and record linking before the reviewed geometry is saved.

A separate River Court example demonstrates private draft saving and initial publication validation. A required English description is initially empty: the draft remains saveable, while publication identifies the affected field. Completing it enables the local publication transition. This demonstrates the distinction between gradual preparation and complete public release.

The enquiry view displays the submitted finishing and price snapshot and supports a processing-status change.

## Administrator scenario

The moderation flow requires a reason to hide Demo Court. The local public catalogue and direct development view then restrict the content, while the owner view displays the reason. Company suspension and reactivation preserve the separate development restriction. Administrator restoration returns the development to display; counts and local event history reflect the changes.

## Screen exports

| Screen | Image | Main design coverage |
| --- | --- | --- |
| Catalogue | [01-catalogue.png](prototype/screens/01-catalogue.png) | Development discovery and floating assistant launcher. |
| Development | [02-development.png](prototype/screens/02-development.png) | Facade and floor entry, with optional sections governed by content availability. |
| Floor | [03-floor.png](prototype/screens/03-floor.png) | Apartment identity, compass and availability states. |
| Apartment | [04-apartment.png](prototype/screens/04-apartment.png) | Plan, characteristics, compact finishing, price and actions. |
| Enquiry | [05-enquiry.png](prototype/screens/05-enquiry.png) | Contact fields and automatically attached selected context. |
| Region review | [06-developer-regions.png](prototype/screens/06-developer-regions.png) | Position correction and reviewed record association. |
| Publication | [07-publication.png](prototype/screens/07-publication.png) | Private draft saving, required translation validation and optional media. |
| Developer enquiries | [08-developer-enquiries.png](prototype/screens/08-developer-enquiries.png) | Submitted context and processing status. |
| Administration | [09-administrator.png](prototype/screens/09-administrator.png) | Visible hiding reason, restoration, counts and action history. |

## Prototype inspection results

Automated interaction checks were completed in headless Microsoft Edge. The [inspection record](prototype/inspection.json) and [reproducible script](../../scripts/inspect_submission_prototype.mjs) document the run. The checks covered the selected price, guest gate, comparison preservation, local enquiry snapshot, region review, publication validation and completion, inbox state, moderation and restoration. Document-width checks covered viewports of 320, 736 and 1024 pixels. The successful run recorded no browser script errors.

These results concern the local design prototype. Section 9 defines the verification protocol for the integrated application and its AI functions.
