# Complete product map and navigation proposal

Review date: 24 October 2026. Features below derive from the stakeholder's description and confirmed decisions. The development-page arrangement (DEC-46), compact finishing selector (DEC-63), unavailable-apartment behaviour (DEC-47) and initial-publication minimum (DEC-64) are approved. Other explicitly proposed placements remain design proposals. This map describes the intended product; it is not evidence of implemented application screens.

## Public navigation and buyer journey

Proposed header: QONYS logo linking to the catalogue, city selector, Comparison, language selector and Account. Favourites and My enquiries remain inside the signed-in buyer account. The floating Find apartment launcher appears on catalogue and property pages. It opens the already-approved assistant overlay, rather than adding another permanent navigation page.

Main journey: Catalogue -> Development -> Building and floor -> Floor plan -> Individual apartment -> Enquiry. The development's Layouts list provides a second path directly to an apartment. The assistant can also return apartment results across developments.

| Screen or function | Responsibility | Access and next step |
| --- | --- | --- |
| Catalogue | Development cards or city map; switch city and open a development. | Guest access. Card and map point lead to the same development. |
| Development overview | Interactive facade/building selector, development description, gallery, construction status and planned completion when applicable. | Guest access. Selecting a floor opens its plan. |
| Layouts within a development | Filter individual apartments by price, area, rooms, building and floor. | Guest access. Results belong only to this development; open an apartment. |
| Floor plan | Building/floor selector, compass, linked apartment regions and availability colours. | Guest access. Select an available apartment. Available has no status fill; reserved is translucent yellow; sold is translucent red. Unavailable apartment details remain viewable through a direct link, but new enquiries are disabled. |
| Apartment | Large plan and characteristics, price, compact finishing dropdown beneath the price (plain text for one condition), corresponding media and optional apartment 3D. | Guest viewing and comparison; sign-in for favourites and enquiry. The developer base is preselected unless valid explicit comparison/AI context selects another offer. Selected finishing carries into comparison and enquiry. |
| Comparison | Compare up to four individual apartments across developments, retaining selected finishing and price. | Guest access. Open the compared apartment or start its enquiry. |
| AI assistant | Collect/clarify preferences, show actual catalogue matches and explain them in the message language. | Guest access. Compact/expanded overlay, full-screen on mobile; opening an apartment minimizes the chat and preserves the current session. Constraint relaxation needs buyer confirmation. |
| Buyer account | Favourites, My enquiries and Account settings. | Verified buyer access. My enquiries shows selected object, date and current processing status. |
| Enquiry form | Contact name, surname, telephone and optional comment; selected apartment/finishing or parking place attached automatically. | Verified buyer access. Save the enquiry and notify the developer through the inbox and SMTP. No payment or automatic reservation. |

## Confirmed development-page arrangement

The development title and a local navigation row appear at the top: Overview, Layouts, Map and infrastructure, Parking, and 3D and panoramas. The facade and building/floor selector occupy the first main overview area, followed by description, characteristics and the gallery. Parking appears only when supplied; developments without parking are valid under DEC-64. The 3D and panoramas section appears only when a usable site model or panorama exists. Its 3D and 360 controls appear independently according to supplied content. Apartment 3D remains on the apartment page beside the selected finishing.

Overview contains the project description, construction information, gallery and optional courtyard/landscaping text. Map and infrastructure contains the development pin and nearby points. These are sections of the selected development, not separate global catalogues. The stakeholder has approved this local navigation arrangement.

## Developer workspace

The four global workspace sections are already approved:

| Section | Responsibility |
| --- | --- |
| My developments | Create/open drafts and published objects; show hidden state/reason. |
| Enquiries | Company-wide apartment/parking inbox, processing states, filters and archive. |
| Company | Company presentation and representative information within agreed permissions. Changes to verified identity remain a policy decision. |
| Account settings | Password/account preferences, interface language and enquiry notification recipient. Detailed identity/recipient changes remain implementation policy. |

Inside a development, the nine approved editing sections are:

| Section | Responsibility |
| --- | --- |
| Basic information | Identity, city/address, construction status, conditional completion quarter/year, optional housing class and cover. |
| Description and gallery | Three-language general text, optional courtyard/infrastructure text and gallery captions/images. |
| Buildings and floors | Building/floor records, facade image and AI-assisted or manually corrected floor regions. |
| Floor plans | Plan images, AI-assisted or manual apartment regions, record links, compass and copying to matching floors. |
| Apartments and finishing | Separate physical apartment records, finishing prices/media, optional apartment 3D, bulk price/status edits. |
| Map and infrastructure | Position, database-backed OSM infrastructure and developer corrections/additions. |
| Parking | Scheme, individual places, interactive links and availability. |
| Site 3D and panoramas | Optional GLB scenes and linked 360-degree panoramic images. |
| Preview and publication | Public-view preview, blocking-issue list and first publication. It is not an extra republish step for later valid saves. |

Preparation journey: Create private draft -> Save sections over multiple sessions -> Review geometry and record links -> Resolve mandatory blockers -> First publication. Once published, valid saved changes are immediately public, subject to administrative restrictions. AI suggestions do not become public before review and save.

## Administrator workspace

The following grouping is proposed; the functions are approved:

| Section | Responsibility |
| --- | --- |
| Overview | Counts of developers, buyers, published developments and hidden developments. |
| Developers | Create access after manual verification; suspend/reactivate developer accounts. |
| Developments | Hide with a reason visible to the owner; restore after correction. |
| Reference data | Edit shared cities and finishing types. |
| Audit history | View and filter automatic records of developer suspension/reactivation, development hiding/restoration and apartment price/availability changes. This function is now approved (DEC-50); the separate menu placement is a design proposal. |

Buyer blocking is explicitly excluded (DEC-51); a buyer count does not create a buyer-management workflow. Audit-history viewing/filtering is approved (DEC-50). Referenced cities and finishing types cannot be deleted; deactivation stops future selection and preserves existing objects and search access (DEC-52). Suspension preserves data and enquiries while hiding developer objects. On administrator reactivation, previously published developments hidden only by account suspension become visible again if otherwise valid; individually hidden objects stay hidden and drafts stay private (DEC-49). One company account, emailed password activation and email recovery are approved (DEC-48).

## Publication completeness

The approved checklist (DEC-64) covers development identity/location/cover/description, declared buildings and floor mappings, residential-floor plans and apartment links, individual apartment characteristics with a 2D layout, developer-configured base condition and price, conditional parking data, and valid ownership/files/links. Separate finishing-option creation is not required (DEC-58); additional variants and example photos are optional. Construction status is required, including planned quarter/year when Under construction. The public-text translation rule is explicitly reconfirmed (DEC-61). Optional 3D, panoramas, additional gallery images and optional descriptions do not block publication solely because absent.

## Review boundaries and remaining material decisions

The confirmed rule for unavailable apartments is to exclude Reserved/Sold apartments from new selection results, retain existing favourites/comparison entries with their current status, and allow direct detail viewing while disabling new enquiries. This does not change the approved floor-plan status colours or make unavailable regions selectable. Existing enquiries are preserved. Submission must recheck current availability rather than relying on an older browser state.

1. Complete remaining buyer-page design details using the approved development-page arrangement, compact finishing selector and publication minimum.
2. Implement the approved minimum-price default, changed-price confirmation, removed-option reselection and enquiry snapshot (DEC-56). Unavailable-apartment behaviour is approved; availability must be checked again on submission.
3. The administrator scope and developer activation/restoration are agreed (DEC-48 through DEC-52). Remaining token, audit-retention and pagination settings belong in implementation design.
4. Specify evaluation and exact model artifacts for the approved initial approaches: Qwen3/Ollama for selection and SAM 2/OpenCV for region research (DEC-53/54). Do not claim quality before measurement. Actual image-source discussion remains deferred.
5. Team titles and Islam Omirzak as supervisor are confirmed (DEC-55). Obtain genuine user/client and supervisor evidence required by the academic stage checklist.

Deployment sizing, file limits, exact SMTP retries and equivalent operational settings belong in implementation design. Their absence does not justify inventing user-facing features or measured results.
