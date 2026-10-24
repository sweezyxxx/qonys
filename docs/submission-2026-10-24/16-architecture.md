# Architecture and diagrams

The architecture combines a Flutter Web client, a modular Django/DRF application, PostgreSQL, file storage and background processing. It supports the approved domain behaviour through explicit ownership, visibility and publication rules.

## Architecture decision

The selected architecture uses one Django/DRF application with logical domain modules and a shared PostgreSQL database. Flutter Web is the browser client. Celery workers execute background tasks delivered through RabbitMQ and reuse the application's domain/data-access rules. Server filesystem storage holds managed uploads and generated geometry files through Django's storage interface; PostgreSQL stores ownership, references, commercial data, visibility and job metadata.

Ollama provides local Qwen3 inference. SAM 2/OpenCV processing uses background workers for project-specific filtering, grouping and SVG conversion. The application retains shared domain rules and data ownership across these execution processes. Long-running operations expose progress and failure states in the interface.

Three.js and Pannellum are embedded client-side viewers for supplied GLB scenes and panoramic JPEG tours. OSM provides external map/data inputs: Flutter uses map tiles, while the application imports infrastructure into retained records and permits developer corrections. SMTP delivers activation, recovery, verification and new-enquiry emails. There is no paid external model provider in the selected baseline.

## Editable diagrams and readable exports

| Figure | Editable semantic source | Readable exports | Purpose |
| --- | --- | --- | --- |
| 1. System context | [Mermaid](diagrams/01-system-context.mmd) | [SVG](diagrams/01-system-context.svg), [PNG](diagrams/01-system-context.png) | Human roles, system boundary and actual external dependencies. |
| 2. Use cases | [PlantUML](diagrams/02-use-cases.puml) | [SVG](diagrams/02-use-cases.svg), [PNG](diagrams/02-use-cases.png) | Guest access, verified-buyer goals, developer preparation and administrator responsibilities. |
| 3. Component architecture | [Mermaid](diagrams/03-components.mmd) | [SVG](diagrams/03-components.svg), [PNG](diagrams/03-components.png) | Client, modular application, shared persistence, workers, local AI and external services. |

The exported figures also have editable geometry JSON. Their generator is scripts/build_submission_diagrams.py. Semantic sources and geometry specifications are maintained together with the readable exports.

## Logical module responsibilities

| Module | Owned responsibilities | Important constraints |
| --- | --- | --- |
| Identity and companies | Buyer registration/verification, sign-in/recovery, administrator-created developer activation, company ownership and account suspension. | One developer account per company; verified buyer access for favourites/enquiries; no public developer registration or buyer blocking. |
| Catalogue and content | Development/building/floor/apartment/finishing records, price/availability, descriptions, media links, geometry links and publication checks. | Private incomplete drafts; complete first publication; valid saves immediately live afterwards; one physical availability state across finishing. |
| Selection | Preference extraction through the local model adapter, parameter validation, permitted catalogue retrieval and grounded explanations. | Visible Available stock only; hard constraints enforced by backend; ambiguity clarified; relaxation requires buyer confirmation. |
| Region preparation | Uploaded-image jobs, SAM 2/OpenCV adapter, candidate geometry, manual edits, record links and prepared-plan copying. | Facade and floor-plan tasks evaluated separately; candidates require developer review; copied floors keep separate apartment identities. |
| Personal features | Buyer favourites, guest comparison and selected finishing context. | Up to four compared apartments; preserve saved unavailable items with current status; never disclose administratively hidden content through saved entries. |
| Enquiries | Availability/finishing/price recheck, accepted enquiry snapshots, developer inbox, buyer history, processing state, archive and notification jobs. | New enquiry is not a reservation; changed price requires confirmation; removed finishing requires reselection; email failure does not erase accepted record. |
| Administration and audit | Developer access control, independent development restrictions, counts, reference lists and key-change audit views. | Reactivation preserves individual restrictions/drafts; referenced values cannot be deleted; no manual audit editing or rollback feature. |

## Main interactions

### Buyer enquiry with a current price

1. The client opens an apartment with its layout and developer-configured base condition/price, preserving a valid explicit comparison/AI selection when present. Extra finishing records are optional (DEC-58/62). Multiple choices use the approved compact dropdown below the price; a single condition is plain text (DEC-63).
2. Before accepting an enquiry, the backend checks verified buyer identity, development visibility, apartment availability, current price and any selected additional finishing. It must not require an extra option record for the base apartment.
3. If price changed, the client presents the updated price for confirmation. If finishing was removed, the client requests another option. If stock became unavailable, the new enquiry is rejected with its current status.
4. Once the request is valid and confirmed, the backend saves contact data, object/finishing context and submitted-price snapshot, and makes the record visible to its buyer and owning developer.
5. Background notification handling attempts SMTP delivery and records its outcome independently of the accepted enquiry. A later price edit preserves the submitted snapshot.

Submission validation and persistence preserve the confirmed commercial context. The interface requests confirmation when the current price differs from the buyer's selection.

### Region preparation and publication

1. An active developer saves an image against an owned building or floor.
2. A processing task references the stored upload and returns candidate geometry/status, not fabricated commercial data.
3. The developer edits geometry and assigns each region to the correct floor/apartment. Manual region preparation remains available if AI fails.
4. Reviewed changes are saved. In a private draft, content remains private. On an already public object, a valid save updates the reviewed public geometry immediately.
5. The initial publication checker covers required fields, translations, files and mappings. No worker result, optional-media upload or ordinary save clears an administrative restriction.

### Independent visibility restrictions

Public development visibility depends on initial publication, an active company account and absence of an individual development restriction. Suspension does not destroy the underlying publication state. Reactivation restores an otherwise valid previously published development hidden only by suspension, keeps individually restricted objects hidden, and never publishes a private draft.

These checks apply to catalogue, maps, direct public detail/API/file access and AI retrieval. Saved favourites and comparison references retain their identifiers while respecting the same public visibility rules. Restricted development content stays protected across all entry points.

## Conceptual data relationships

| Relationship | Integrity requirement |
| --- | --- |
| Company -> Development -> Building -> Floor -> Apartment | Each object has the correct owned parent; identifiers cannot be substituted across companies or floors. |
| Apartment -> Optional additional finishing options | The apartment has a usable layout, developer-configured base condition and price without extra records. Additional variant price/description/media/3D belong to that option; availability belongs to the physical apartment. |
| Building image -> Floor region -> Floor | A reviewed region opens its assigned floor in the same building. |
| Floor plan -> Apartment region -> Apartment | A reviewed region maps to a complete apartment record, not merely a room-shaped mask. |
| Floor plan template -> Target floor plans | Geometry can be copied while physical apartment identities remain separate. |
| Development -> Parking scheme -> Place | The place and enquiry context belong to the correct development/company. |
| Buyer + selected object/finishing -> Enquiry | Access is limited to the buyer and owning company; submitted commercial context is preserved historically. |
| Actor + object + successful change -> Audit record | The audit entry retains the approved key event, timestamp and relevant change values, excluding secrets and contact payloads. |
| City/finishing reference -> Referencing records | Deactivation prevents future assignment and preserves existing use/search; referenced-value deletion is blocked. |

The relationship model defines the ownership and integrity rules that guide database tables, constraints and API contracts.
