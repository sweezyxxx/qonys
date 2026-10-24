# Requirements and acceptance criteria

Baseline: 24 October 2026, based on decisions DEC-01 through DEC-65. The matrix defines functional and non-functional behaviour, initial implementation priorities and verifiable acceptance criteria. The first-publication minimum is consolidated below. Scenario checks are defined in the evaluation plan.

Priority meaning: Must = needed for a core workflow or an explicit constraint; Should = useful supporting capability in the approved scope, scheduled after the core path; Conditional = required when the developer supplies the optional feature. A Should priority does not remove an approved feature. Excluded functions remain excluded.

## Accounts and access

| ID | Requirement | Priority | Verifiable acceptance |
| --- | --- | --- | --- |
| FR-01 | Provide buyer email/password registration, sign-in and email password recovery; require registration email verification before account access. | Must | An unverified registrant can browse as a guest but cannot enter buyer-only functions. Verification enables account access; a valid recovery flow permits password reset. |
| FR-02 | Allow guests to browse, compare apartments and use AI selection. Require verified buyer sign-in for favourites and new enquiries. | Must | The same guest can open catalogue/detail/comparison/assistant screens; favourite and enquiry actions require verified sign-in and cannot be bypassed through direct API requests. |
| FR-03 | Allow an administrator to create one developer account per manually verified company, with email password activation and recovery. | Must | The representative sets a password through the issued link and accesses the company workspace. Public company self-registration and staff-account workflows are absent. |
| FR-04 | Enforce role and ownership boundaries across data and file access. | Must | Developer A cannot access or mutate Developer B's private drafts/files/enquiries; a buyer can view only their own enquiry history. Changing a requested object identifier does not bypass these checks. |

## Catalogue and buyer navigation

| ID | Requirement | Priority | Verifiable acceptance |
| --- | --- | --- | --- |
| FR-05 | Show a shared development catalogue for a selected city in list and map modes. | Must | Both modes use the same eligible published developments; card and marker open the corresponding development. Hidden developments do not appear. |
| FR-06 | Provide the approved development-page arrangement and local navigation. | Must | Title and navigation appear at the top; Overview starts with interactive facade/building/floor selection, followed by description, characteristics and gallery. Absent optional sections are hidden. |
| FR-07 | Link building-image floor regions to the correct floor plans. | Must | Selecting a region on Building A, Floor F opens A/F rather than a similarly numbered floor in another building. The floor summary is derived from its apartment records. |
| FR-08 | Display floor plans, compass and linked apartment availability regions. | Must | Available regions have no status fill, Reserved regions have translucent yellow fill and Sold regions have translucent red fill. The available-apartment action opens the correct individual record. |
| FR-09 | List separate individual apartment cards with development-local filters. | Must | Apartments sharing a plan on different floors remain separate records/cards. Price, area, rooms, building and floor filters do not retrieve another development's stock. |
| FR-10 | Show the apartment's 2D layout, developer-configured base condition, characteristics and price without requiring extra finishing records; support optional variants. | Must | A base apartment works with no extra variants or example photos. Its condition may be No finish, WhiteBox, finished or another supported developer selection; absence of media never assigns a false default. Multiple choices use a compact dropdown below the price, labelled with condition and full price; a single condition uses text. The base is initially selected unless valid explicit comparison/AI context supplies another offer. Changing the choice updates its price, description and supplied media while preserving physical identity/availability and carrying the choice into comparison/enquiry (DEC-63). |
| FR-11 | Maintain one availability state per physical apartment across finishing options. | Must | Marking an apartment Sold does not leave another finishing option Available for that physical apartment. |
| FR-12 | Exclude Reserved/Sold apartments from new selection results while retaining existing favourites/comparison with current status. | Must | After a status change the apartment disappears from new results but remains in prior saved selections. A direct detail link remains readable for an otherwise public development, and its new-enquiry action is disabled. |
| FR-13 | Compare up to four individual apartments across developments/developers, retaining selected finishing and preserving guest comparison at sign-in. | Must | A fifth item is not added. Each displayed item identifies its development/developer/location, rooms, area, floor, bathrooms, selected finishing, corresponding price and availability. Signing in preserves the guest comparison entries (DEC-65). |
| FR-14 | Provide buyer Favourites, My enquiries and Account settings. | Must | A verified buyer can reopen a favourite and view their enquiry object, submission date and current processing status. Name, surname and phone are optional before an enquiry needs them, editable in settings and prefilled/correctable in the enquiry. Password can be changed; email is displayed without an address-change workflow (DEC-65). Comparison remains separately accessible to guests. |

## Developer content and publication

| ID | Requirement | Priority | Verifiable acceptance |
| --- | --- | --- | --- |
| FR-15 | Provide four developer workspace sections and nine editing sections inside a development. | Must | Workspace navigation contains My developments, Enquiries, Company and Account settings. Each development contains Basic information, Description and gallery, Buildings and floors, Floor plans, Apartments and finishing, Map and infrastructure, Parking, Site 3D and panoramas, and Preview and publication. |
| FR-16 | Persist incomplete private drafts across sessions and allow gradual section saving/uploading. | Must | A developer saves incomplete content, signs out/in and resumes it. The incomplete development is not publicly accessible. Autosave is not assumed. |
| FR-17 | Require construction status and planned completion quarter/year when Under construction. | Must | Initial publication rejects missing status and an under-construction record missing the planned quarter/year. Housing class is optional. |
| FR-18 | Use structured descriptions/gallery and require three languages for all populated public development, apartment, finishing and company descriptions and gallery captions. | Must | Private incomplete translations can be saved; public descriptions/captions require Russian, Kazakh and English. Proper names, addresses and identifiers are exempt. No automatic translation is assumed. |
| FR-19 | Gate first publication on the complete required field/file/link checklist. | Must | The preview lists each validation issue and its editing section. All mandatory data and links satisfy the First publication criteria below. Extra finishing variants, example photos, 3D and panoramas are optional. Parking data is required only when parking is offered; no minimum infrastructure-point count is imposed. |
| FR-20 | Make valid saved changes immediately public after first publication, respecting administrative restrictions. | Must | A saved valid price/text/plan/media change is reflected without a republish step. Saving does not clear an administrator hide or publish unreviewed AI candidates. |
| FR-21 | Copy prepared plans/regions to matching floors while preserving separate physical stock. | Should | Copied geometry can be reused, but target apartments have separate identities, numbers, prices and availability; the developer reviews target links. |
| FR-22 | Support bulk apartment price/availability editing within the apartment list. | Should | A selected set of owned apartments receives the valid update; unselected apartments and other developers' records remain unchanged. |

## AI selection and region preparation

| ID | Requirement | Priority | Verifiable acceptance |
| --- | --- | --- | --- |
| FR-23 | Use local Qwen3/Ollama to interpret buyer text into supported structured preferences. | Must | Each multilingual test case compares extracted fields with independently defined expected fields. Backend validation rejects unsupported values; acceptance depends on field correctness and valid catalogue results. |
| FR-24 | Respect hard constraints, clarify important ambiguity and explain matches from known catalogue/infrastructure facts. | Must | Returned records satisfy the validated hard constraints; ambiguous important input prompts clarification. Missing data is not asserted as verified. Constraint violations and unsupported claims are reported as defects. |
| FR-25 | State empty exact results and obtain confirmation before relaxing a condition. | Must | An over-constrained request produces no fabricated matches. A proposed specific change does not trigger relaxed results until the buyer accepts it. |
| FR-26 | Provide the floating compact/expanded assistant, mobile screen view and current-session continuity. | Must | Opening an apartment minimizes the assistant; reopening retains the current conversation/conditions. Browser-restart persistence is not an acceptance requirement. |
| FR-27 | Investigate automatic floor/apartment candidates using SAM 2/OpenCV and project-specific processing. | Must; research risk | Facade and floor-plan cases are evaluated separately using candidate geometry, grouping errors, reviewed record links and correction effort. A successful apartment candidate covers the intended apartment rather than unrelated rooms or objects. The evaluation records per-case results against a manual reference. |
| FR-28 | Provide manual region addition/editing/deletion and explicit floor/apartment assignment. | Must | A developer can correct or replace an unsuitable suggestion, link it to the correct owned record and save it. Unreviewed candidates do not become public. |

## Maps, parking and optional viewers

| ID | Requirement | Priority | Verifiable acceptance |
| --- | --- | --- | --- |
| FR-29 | Use OSM/flutter_map for development locations and database-backed infrastructure that developers can correct/supplement. | Must | A development pin matches saved coordinates; supported nearby categories are displayed from retained records and permitted corrections appear. Displayed infrastructure reflects the saved source records and developer corrections. |
| FR-30 | Provide interactive parking-place availability and place-specific enquiries when parking is offered. | Conditional | An available place opens an enquiry with the correct identifier; an unavailable place cannot be selected. The flow contains no payment or automatic reservation. |
| FR-31 | Display developer-supplied optional site/apartment GLB content with Three.js. | Conditional | A supported valid supplied scene permits rotation, zoom and camera-angle changes. A missing scene hides its public action. Full collision-aware first-person navigation is not required. |
| FR-32 | Display optional panoramic JPEG tours with Pannellum. | Conditional | A supplied panorama permits looking around and configured transitions between points. With no valid supplied panoramas the corresponding action is hidden. |

## Enquiries and administration

| ID | Requirement | Priority | Verifiable acceptance |
| --- | --- | --- | --- |
| FR-33 | Create verified-buyer enquiries with contact data, selected object/presentation and submitted-price snapshot. | Must | The server rechecks identity, visibility, availability and current price. An extra finishing selection is checked only when used; no extra variant is required for the default apartment. A changed price requires confirmation; a removed selected variant requires a valid replacement. Accepted submitted context remains historical. No reservation occurs. |
| FR-34 | Deliver new enquiries to the owning developer inbox and queue SMTP notification independently of record persistence. | Must | After an accepted submission the enquiry is in the correct inbox. A simulated email failure does not erase it or require the buyer to recreate an already accepted record. |
| FR-35 | Support developer-managed New, In progress, Processed and Cancelled enquiry states and archive viewing. | Must | Status changes appear in the buyer's history without changing apartment availability. Archived completed records remain viewable; developer permanent deletion is absent. |
| FR-36 | Allow administrator hiding with a developer-visible reason and administrator-controlled restoration. | Must | Hidden development content is absent from list/map/AI/direct public access. The owner sees the reason. Ordinary saves cannot restore public access. |
| FR-37 | Suspend/reactivate developer access using separate company and individual-development restrictions. | Must | With previously published A, individually hidden B and draft C, suspension hides all public company content. Reactivation restores eligible A, leaves B hidden and keeps C private. Data/enquiries remain. |
| FR-38 | Provide counts of developers, buyers, published developments and hidden developments. | Should | Counts match the controlled fixture under the documented counting definitions. The buyer summary provides a count without buyer account-blocking controls. |
| FR-39 | Allow city/finishing reference editing and deactivation while protecting referenced values from deletion. | Must | Referenced-value deletion is rejected. Deactivation prevents new assignments while existing records display their value and remain findable. |
| FR-40 | Automatically record key successful changes and provide administrator audit viewing/filtering. | Should | Suspension/reactivation, hide/restore and apartment price/availability updates produce an attributed, timestamped record for the correct object. Ordinary users cannot edit the history. |

## Non-functional requirements

The quality requirements cover ownership, data integrity, language support, responsive interaction, enquiry durability, publication safety, confidential data, reproducible dependencies and maintainability. Each requirement has a concrete verification method.

| ID | Requirement | Priority | Planned acceptance method |
| --- | --- | --- | --- |
| NFR-01 | Enforce server-side roles, ownership and publication visibility consistently. | Must | Negative API, file and direct-link tests cover the guest, buyer, unrelated developer, owner and administrator roles. Any unauthorized private-object disclosure or mutation fails the affected requirement. |
| NFR-02 | Preserve catalogue identity and relationship integrity. | Must | Integrity checks cover plan/region/apartment associations, separate stock on copied floors and shared availability across finishing. Invalid cross-owner/cross-floor mappings must not be saved as valid public content. |
| NFR-03 | Support Russian, Kazakh and English system UI, buyer AI and approved public descriptions/captions. | Must | Critical scenarios in each language check labels, validation/state messages, assistant reply language and all populated public descriptions and captions, with the defined proper-name/address/identifier exemptions. |
| NFR-04 | Provide usable desktop and mobile browser layouts for critical flows. | Must | Catalogue, floor selection, apartment, assistant, comparison and developer editing are checked at the target viewport/browser profiles recorded for the run. No essential action relies on hover alone; navigation and required content remain reachable without overlap. |
| NFR-05 | Keep accepted enquiries durable despite email-delivery failure. | Must | A simulated SMTP failure after acceptance leaves the enquiry accessible in the buyer and developer views. Delivery recovery preserves the same enquiry identity and submitted context. |
| NFR-06 | Keep first-publication completeness and administrative restrictions independent from media/AI jobs. | Must | Failure or partial completion of a background job does not make an incomplete draft public or clear a restriction. The developer can return to manual correction. |
| NFR-07 | Protect authentication and confidential data in persistence, responses and audit history. | Must | Security checks cover password storage, reset-token handling and representative API/audit outputs. Outputs contain no passwords, reset tokens or contact data outside the permitted audience. |
| NFR-08 | Use free AI model/runtime dependencies and document exact reproducible artifacts. | Must | The implementation acceptance record includes licences, checkpoint/digest, runtime/dependency versions, configuration and the resource profile. No paid model API is required by the selected approach. |
| NFR-09 | Verify operation under the intended single-user demonstration profile and record observed responsiveness. | Must | Selected end-to-end scenarios complete under the stated single-user browser, hardware and code version. The run records blocking failures and observed response times where measured. This profile evaluates demonstration readiness rather than concurrent-user capacity. |
| NFR-10 | Keep implementation and documentation traceable and maintainable. | Must | Requirement references connect design elements, YouTrack tasks and verification evidence. Editable diagrams, identifiable contributions and versioned decisions preserve traceability. |

## Scope boundaries and shared rules

Excluded: developer chatbot, interior generation, document-based question answering/RAG, automatic 3D reconstruction, payments, automatic reservations, buyer blocking, separate company employee accounts and a native mobile app deliverable.

The requirements retain one physical-apartment identity across finishing offers, developer-configured base finishing, a compact selector, three-language descriptions and the distinction between private drafting and complete initial publication.

## First publication criteria

A developer can save a private development gradually. Initial publication is allowed when all applicable mandatory checks pass. The preview links each validation issue to its editing section. After publication, valid saved changes are visible immediately.

| Area | Mandatory publication data |
| --- | --- |
| Identity and location | Name, city, address, map coordinates and cover image. |
| Public text | Development description in Russian, Kazakh and English. Every populated public description and gallery caption has all three versions; proper names, addresses and identifiers are exempt. |
| Construction | Construction status; planned completion quarter and year when Under construction. |
| Buildings and floors | All declared buildings and residential floors, supplied facades and floor plans, and valid floor/apartment region links. |
| Apartments | Number, building and floor, room count, area, bathroom count, 2D layout, developer-configured base finishing condition, base price and availability. |
| Parking | Plan, place identifiers, availability and applicable commercial information when parking is offered. |
| Optional content | Extra finishing offers, example photos, 3D assets, panoramas and a minimum infrastructure-point count are not publication prerequisites. |

Optional content that is supplied satisfies its relevant validation rules. An administrative restriction remains independent from publication completeness and cannot be cleared by the developer's save operation.
