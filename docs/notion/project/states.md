# State Models and Integrity

Business lifecycle states have different owners and must not be collapsed into a single status field. Development preparation, administrative visibility, physical availability, enquiry processing and background processing are independent concepts.

## Development visibility

Public display requires all of the following: initial publication has succeeded, the company account is active, and no individual development restriction is in effect. The same decision governs catalogue, maps, AI, details and files.

| Event | Content/publication effect | Restriction effect |
| --- | --- | --- |
| Save an incomplete new development | Persists a private draft | No restoration or public release. |
| Publish a complete eligible development | Establishes initial publication | Cannot bypass company/individual restrictions. |
| Save a valid later change | Updates the public content immediately when eligible | Existing restrictions remain. |
| Hide a development | Preserves underlying content/publication | Individual restriction with an owner-visible reason. |
| Suspend company | Preserves all content, drafts and enquiries | Hides the company's public developments and blocks developer operations. |
| Reactivate company | Makes eligible previously published developments visible again | Individual hides remain; drafts remain private. |
| Restore individual development | Removes its individual hide | Company suspension can still prevent public access. |

## Physical availability

Available, Reserved and Sold belong to the physical apartment, not to each finishing offer. Reserved/Sold records are excluded from new selection, retained in existing saved selections with current status, and cannot accept a new enquiry. Direct details remain readable only when the development is public.

Parking uses its own availability. Neither submitting an enquiry nor processing it automatically changes apartment/parking availability.

## Enquiry processing

New, In progress, Processed and Cancelled describe the developer's handling of the enquiry. Archive state controls the developer's completed-record view rather than deleting the enquiry or removing buyer history. The baseline does not define a universal transition/reopening rule beyond the stated processing and archive behaviours.

## Region review and background state

Processing progress/failure indicates whether a task produced candidate output. Developer review indicates whether geometry and record links are accepted. A successful task does not turn an unreviewed candidate into published geometry.

## Required integrity rules

1. Company → Development → Building → Floor → Apartment ownership is consistent on every write and read.
2. A facade region references a floor in its source building; a floor-plan region references an apartment on its source floor.
3. Copying geometry never reuses the same physical apartment identity on multiple floors.
4. All finishing offers share the apartment's availability.
5. Enquiry acceptance validates the current commercial state and preserves the confirmed snapshot as part of persistence.
6. Referenced city/finishing values survive deactivation and cannot be deleted while referenced.
7. Required translations/files/mappings are checked for first publication and for valid public saves.
8. Worker output and ordinary content saves cannot remove administrative restrictions.

[[publication]], [[apartments]], [[enquiries]] and [[administration]] own the operations that apply these rules. [[verification]] covers both successful and rejected paths.
