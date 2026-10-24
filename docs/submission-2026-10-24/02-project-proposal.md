# Project proposal

## Project title

Development of an AI-Powered Residential Real Estate Visualization and Intelligent Property Selection Platform with 3D Site Visualization, Floor-Level Layouts, and Interactive Mapping

## Team and supervisor

Temirlan Almukhamedov is the Systems Analyst and Technical Coordinator. Yevgeniy Averyanov is responsible for backend development. Bexultan Nishanbek is responsible for Flutter Web and frontend development. Islam Omirzak is the supervisor.

## Problem statement

Apartment buyers need to compare properties across different developers using price, area, room count, floor, finishing and location. Relevant information is often presented in separate development websites, listing pages, building images, floor plans and maps. Buyers must connect these materials themselves to understand where a particular apartment is located, whether it is available and how it compares with other offers.

Developers also need to maintain the links between building photographs, floor plans and apartment records. Preparing selectable floor and apartment regions manually requires tracing boundaries and assigning each region to the correct record. Automated suggestions may reduce this effort, but incorrect boundaries or record links require review and correction before publication.

QONYS addresses these tasks through one catalogue with interactive building and floor images, structured apartment information, cross-development comparison, infrastructure maps and natural-language property selection. The evaluation plan defines how the integrated workflow and AI-assisted region preparation will be assessed against manual baselines at a comparable final quality level.

## Target users

Buyers use the platform to explore residential developments, inspect floors and apartment layouts, compare offers, save favourites, examine the surrounding infrastructure and send enquiries.

Property developers manage their own developments, buildings, floors, apartments, parking and supporting visual material. They review AI-suggested regions, correct their geometry, assign catalogue records and handle enquiries through their workspace.

Platform administrators create developer accounts after manual verification and can suspend or restore developer access. They can hide a development with a reason visible to the developer and restore its public display after correction. Suspending a developer hides all of its developments while preserving data and enquiries. Developers publish their own reviewed materials, but cannot bypass an administrative restriction. Administrators also edit city and finishing-type reference lists and view counts of developers, buyers, published developments and hidden developments. Realtors are outside the defined roles.

The first version uses one developer account per company. An emailed activation link lets the representative set their own password after administrator account creation; password recovery also uses email. On account reactivation, previously published developments hidden only by company suspension return to public display if otherwise valid. Individually hidden developments retain their restriction, and private drafts remain private.

Administrators can view and filter automatic audit records for developer suspension/reactivation, development hiding/restoration and apartment price/availability changes. Referenced cities and finishing types cannot be deleted; they can be deactivated for future selection while existing objects and their search access are preserved. Buyer blocking is outside the first version.

## Aim

The aim is to develop a residential property platform that helps buyers select and compare apartments across developers using structured catalogue information, natural-language preferences, interactive building images, floor-level layouts, optional developer-supplied 3D visualizations and infrastructure maps, while helping developers prepare and maintain interactive floor and apartment regions with AI assistance and manual correction.

## Objectives

1. Investigate buyer and developer needs through user/client discussions and a critical review of related systems and research.
2. Develop a catalogue of residential complexes from different developers with city selection and consistent list/map views.
3. Implement navigation from a development and building to a selected floor plan and a linked apartment record.
4. Provide apartment details, finishing choices, favourites and comparison across residential developments and developers.
5. Implement a buyer selection tool that interprets natural-language preferences, retrieves actual catalogue properties and explains their relevance.
6. Develop and evaluate AI-assisted suggestions for visible floor regions on building images and apartment regions on floor plans, including manual correction and record assignment.
7. Integrate development location and nearby infrastructure information using a cartographic service and an agreed data source.
8. Support the upload and display of optional site 3D scenes, linked 360-degree panoramas and apartment 3D models supplied by developers.
9. Provide developer content management, administrator-managed developer access and internal apartment/parking enquiries.
10. Define and execute functional, access-control, usability, recommendation and content-preparation evaluations, distinguishing planned targets from observed results.

## Expected outcomes

The final project deliverable is an integrated application prototype covering the main buyer, developer and administrator scenarios. Buyers will be able to move from the catalogue to a development, building, floor and apartment, compare records and send an enquiry associated with the chosen property and finishing option. Developers will be able to maintain their own property information, visual material, region mappings and enquiry statuses.

Developers can save private development drafts and fill them gradually. A development is published as a complete object only after all mandatory information and mappings are ready; partial public publication is excluded. Optional 3D models and panoramas are not prerequisites for an otherwise complete development. Description content uses defined text fields and a gallery with optional captions; every populated description/caption must be complete in Russian, Kazakh and English before publication.

Construction status is required; an under-construction development also provides a planned completion quarter and year. Housing class is optional. First-publication criteria are consolidated in the requirements section.

After initial publication, all valid saved changes become visible immediately, including descriptions, plans, media, prices and availability. There is no additional republish step. The apartment list supports bulk price and availability updates. The workspace contains My developments, Enquiries, Company and Account settings, with dedicated editing sections inside each development.

The AI design combines catalogue-based buyer selection with editable image-region suggestions and a manual preparation path. The evaluation plan covers region quality, correction effort, record-link correctness, preparation time, workflow completion and compliance with mandatory buyer preferences.

The work completed for 24 October comprises the proposal, analysis of three interviews, literature and system comparisons, a requirements matrix with acceptance criteria, three architectural diagrams, an interactive design prototype, and verification and delivery plans. The following scope describes the application specified by these materials.

## Project scope

### Catalogue and buyer navigation

The main page shows residential complexes for the selected city in list or map mode. A development contains one or more buildings. Selecting a visible floor region on a building image opens the associated floor plan. Apartment regions refer to separate catalogue records; apartment price, area and availability are entered by the developer rather than inferred from an image.

A development's layout section filters apartments within that development and displays individual apartment cards rather than grouping identical layouts across floors. The natural-language selection tool operates across the platform catalogue. Buyers can compare up to four apartments from different developments and developers by development, developer, location, room count, area, floor, bathrooms, selected finishing, price and availability. The selected finishing option and its price remain part of the comparison context. Guests can browse, use AI selection and compare apartments. Favourites and enquiry submission require buyer sign-in. Buyers use email and password with email-based recovery and must verify their email during registration before account access is granted.

The development page has its title and local navigation at the top: Overview, Layouts, Map and infrastructure, Parking, and 3D and panoramas. Overview starts with the interactive facade and building/floor selection, followed by description, characteristics and gallery. Absent optional sections are hidden. Reserved and Sold apartments are excluded from new selection results but retained in existing favourites/comparison with their current status. Direct apartment-detail links remain viewable; new enquiries are disabled while unavailable and current availability is checked on submission.

### Apartment information and enquiries

Apartment information includes the supplied 2D layout, room count, area, bathrooms, building, floor, developer-configured base finishing condition, price, availability and other supported characteristics. The base condition may differ between developments; it is not hardcoded as finished delivery or inferred from uploaded media. Extra finishing variants and example photos are optional, so the base apartment remains usable without additional option records. Additional variants can have their own price, description, images and optional 3D model, while physical availability remains shared. A compact dropdown beneath the price selects among offered conditions; a single condition is shown as text. The base condition is initially selected unless a valid explicit comparison or AI context identifies another offer. The selection retains its context in comparison and enquiries.

An apartment with no additional variant uses its own 2D layout and price; no separately entered default-finishing record is required. An explicit comparison/AI presentation context is retained. An enquiry uses the current base/selected-variant price: a changed price requires confirmation, a removed selected option requires a valid replacement, and submission records the presentation and price as a historical snapshot. Public descriptions are stored in Russian, Kazakh and English; supplied images retain their original content. Private drafts support gradual entry of the three text versions.

Public manager telephone numbers are not displayed. An enquiry form collects buyer contact information and an optional comment; the selected object is attached automatically. The developer workspace shows enquiries for that developer's objects and new enquiries trigger SMTP email notifications. Developers update enquiry processing through New, In progress, Processed and Cancelled states and can archive completed enquiries for later viewing. Permanent deletion by the developer is excluded from the first version. Buyers can view their own enquiries, including the object, submission date and current processing status, in their account alongside Favourites and Account settings. Buyer profile name, surname and phone are optional before the first enquiry, editable in settings and prefilled in the enquiry form, where the buyer can correct them. Password can be changed; email is displayed without an address-change workflow. Signing in preserves the guest comparison list. Sending an enquiry does not reserve, purchase or pay for a property.

Parking uses an interactive scheme. Available spaces can be selected to send an enquiry; unavailable spaces cannot be selected. Payment and automatic parking reservation are outside scope.

### AI-assisted region preparation

A developer uploads a building image or floor-plan image. The system proposes editable regions for visible floors or apartments, respectively. The developer reviews the result, moves or adds boundaries where needed, removes incorrect regions and assigns each region to a floor or apartment record.

A prepared floor plan and its reviewed SVG regions can be copied to matching floors. Each target floor has separate apartment identities, numbers, prices and availability, and the developer checks the copied associations before publication.

Facade recognition and apartment-region recognition are separate tasks. A visible facade does not provide the internal floor plan. Detecting rooms does not automatically establish the full boundaries or catalogue identity of an apartment. The design therefore separates candidate geometry, developer correction and reviewed record assignment. The evaluation plan assesses the two image tasks separately.

### Intelligent buyer selection

The buyer describes preferences in Russian, Kazakh or English. The AI interprets the text into supported parameters and the backend checks actual catalogue properties against explicit city, budget and other hard constraints. Stated preferences affect result ordering. Explanations use available catalogue and infrastructure evidence. If no exact matches exist, the system states this and proposes a specific constraint change; a new search follows buyer confirmation. The assistant responds in the language of the buyer's message independently of the interface language.

A floating button on public catalogue and property pages opens a compact chat overlay. The expanded desktop view places conversation and conditions beside apartment results; the mobile view occupies the screen. Opening an apartment minimizes the assistant and retains the current session context. The interface supports Russian, Kazakh and English; developer-supplied public descriptions use all three languages. Private drafts support gradual translation entry. The selected approach uses local Qwen3 through Ollama with server-side preference validation.

The assistant does not answer questions by retrieving uploaded developer documents. A developer chatbot is also excluded.

### Optional visual material

The platform supports three independent types of developer-supplied material: an interactive 3D scene of the site and buildings, linked 360-degree panoramas, and an apartment 3D model, which may show an unfinished space or a prepared interior. The corresponding interface section is displayed only when usable material exists.

Developer-supplied scenes use GLB and Three.js with rotation, zoom and camera-angle changes. Panoramic JPEG images use Pannellum for looking around and moving between points. Both viewers are embedded in Flutter Web. Optional 3D content complements the required image-based floor and apartment navigation.

### Technical baseline and exclusions

The baseline is Flutter Web, Django with Django REST Framework, PostgreSQL, Celery and RabbitMQ. The application architecture is a modular monolith with shared PostgreSQL and background workers. Managed uploads use server filesystem storage through Django, with ownership, references and metadata in PostgreSQL. Maps use OpenStreetMap and flutter_map; infrastructure records are retained in the platform database and can be corrected or supplemented by the developer. Visual viewers use Three.js and Pannellum. Buyer selection uses local Qwen3 through Ollama. Region preparation combines SAM 2/OpenCV with project-specific processing and SVG conversion.

AI implementation uses free solutions without paid model API or licence dependencies. The evaluation covers model resource fit, catalogue constraint compliance and image-region correction effort. SAM 2 supplies generic segmentation suggestions; project-specific processing and reviewed record assignment connect them to complete apartments and facade floors.

Property transactions, mortgage processing, payments, automatic reservations, a developer chatbot, interior-design generation, document-based question answering and automatic 3D reconstruction are outside the project scope. A native mobile application is not included in the current browser-based deliverable.
