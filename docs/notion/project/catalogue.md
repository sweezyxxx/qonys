# Catalogue and Spatial Navigation

The catalogue connects development discovery to an identifiable physical apartment. It owns city-scoped list/map discovery, development-local apartment filtering and the building/floor navigation path.

Requirements: FR-05–FR-09, FR-12 and NFR-02/NFR-04. See [[requirements]].

## Discovery

The selected city scopes the shared catalogue across developers. List cards and map markers represent the same eligible developments and open the same development record. Administratively restricted developments are excluded from both modes and from AI retrieval.

A development's Layouts section filters only its own physical apartments by price, area, room count, building and floor. Apartments with a shared layout on different floors remain separate cards. Comparison and AI selection can span developments.

## Development page

The title and local navigation appear above the main content: Overview, Layouts, Map and infrastructure, Parking, and 3D and panoramas. Overview begins with the interactive facade and building/floor selector, followed by description, characteristics and gallery. Optional sections appear only when their content exists.

## Facade to floor

A reviewed region belongs to a building image and references a floor in that same building. Selecting it opens that floor's plan. Floor summaries are derived from the floor's apartment records, rather than maintained as independent commercial facts.

The facade image does not supply the internal layout. Building/floor links and the floor-plan apartment links are separate mappings reviewed in [[regions]].

## Floor to apartment

The floor view provides a building/floor selector, supplied plan, compass and apartment regions. An Available region has no status fill; Reserved uses translucent yellow and Sold uses translucent red. Only an available region provides the new-selection action.

Reserved/Sold apartments disappear from new selection results. Existing favourites and comparisons retain the apartment with its current status. A direct detail link remains readable for a public development, while new enquiries are disabled. Administrative hiding is a stronger restriction and applies to those direct reads too.

## Integrity and acceptance

- A region on Building A, Floor 5 must not open Floor 5 in Building B.
- A floor-plan region opens its assigned physical apartment, not another apartment sharing its plan.
- List and map results agree on development eligibility.
- Changing an apartment's availability updates selection eligibility across all finishing offers.
- Catalogue and floor navigation remain usable on mobile without essential hover-only actions.

[[apartments]] owns apartment offers and comparison. [[states]] defines visibility and commercial state; [[navigation]] defines screen responsibilities.
