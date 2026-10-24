# Navigation and Screen Responsibilities

The UI organises the same domain records into public discovery, buyer account, developer workspace and administrator workspace. Screen placement does not change access or publication rules.

## Public and buyer navigation

The header provides the QONYS catalogue entry, city selector, Comparison, language selector and Account. The floating Find apartment launcher appears on catalogue and property pages. Favourites and My enquiries are inside the verified buyer account.

| Screen | Primary responsibility | Continuity |
| --- | --- | --- |
| Catalogue | City-scoped development cards/map | Card and marker resolve the same development. |
| Development Overview | Facade/building/floor entry, descriptions, characteristics and gallery | Local navigation retains the development. |
| Layouts | Filter separate apartments within the development | Opens an individual physical apartment. |
| Floor plan | Plan, orientation, region links and status colours | Building/floor selection resolves the correct plan. |
| Apartment | Plan, characteristics, condition, full price and actions | Selected finishing carries into comparison and enquiry. |
| Comparison | Up to four apartment/offer selections | Guest selection survives sign-in. |
| Assistant | Conversation, conditions and catalogue result cards | Opening a result minimises chat and retains current-session context. |
| Enquiry | Correctable contact details and selected object/offer | Accepted snapshot becomes available in buyer history and developer inbox. |

Development-local sections are Overview, Layouts, Map and infrastructure, Parking, and 3D and panoramas. Optional sections are hidden when no applicable content exists. Apartment-specific 3D belongs to the apartment presentation.

## Developer workspace

Global sections are My developments, Enquiries, Company and Account settings. The development editor contains:

| Section | Content and action |
| --- | --- |
| Basic information | Identity, city/address/coordinates, construction status, planned quarter/year, optional class and cover. |
| Description and gallery | General and optional courtyard/infrastructure text, three language versions, gallery images/captions/order. |
| Buildings and floors | Structure, floor numbering, facades, candidate floor regions and record links. |
| Floor plans | Plan images, apartment regions, compass, corrections and repeated-floor copying. |
| Apartments and finishing | Individual stock, characteristics, base and extra offers, applicable models and bulk edits. |
| Map and infrastructure | Development point and retained infrastructure corrections/additions. |
| Parking | Scheme, places and availability when offered. |
| Site 3D and panoramas | Optional site scenes and linked tour points. |
| Preview and publication | Buyer preview, section-linked blockers and complete initial publication. |

Save belongs to the affected section. Processing progress/errors appear with the relevant image. A hiding reason appears with the development state. Enquiries remain company-wide rather than being trapped inside a single development editor.

## Administrator workspace

Overview contains counts; Developers controls company admission and access; Developments controls hiding/restoration; Reference data manages cities/finishing types; Audit history presents the defined key events. Buyer blocking is absent.

## Interaction rules

The finishing selector is compact and below the price, with plain text when only one condition exists. The assistant has compact/expanded desktop layouts and a mobile screen view. Important floor/apartment actions remain available without hover-only interaction. Validation identifies the affected field or editing section.

The interactive HTML and nine screen exports in [[defence-prototype]] provide the current design reference. Module behaviour is defined in [[catalogue]], [[apartments]], [[publication]] and [[administration]].
