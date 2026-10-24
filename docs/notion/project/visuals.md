# Maps Parking and Visual Assets

These features add location context, selectable parking and optional supplied visual material to the required building/floor/apartment path. The absence of optional 3D or panoramic content does not prevent an otherwise complete development from publication.

Requirements: FR-29–FR-32. See [[requirements]].

## Maps and infrastructure

Flutter Web uses flutter_map with OpenStreetMap sources. The saved development coordinates identify its map pin. Infrastructure points are retained in the platform database and can be corrected or supplemented by the owning developer. Displayed categories include the supported schools, kindergartens, shops, shopping centres and parks.

The map and assistant use available saved facts. Missing source coverage is not presented as proof that a facility does not exist. No minimum infrastructure-point count gates publication. Public markers and development reads follow the same visibility rules as the catalogue.

## Parking

When parking is offered, the development has a supplied scheme, linked place identifiers, availability and applicable commercial information. An available place opens an enquiry with that exact place context. An unavailable place cannot be selected. Parking availability and enquiry processing are distinct states; no payment or automatic reservation is performed.

## Optional viewers

| Content | Viewer and interaction | Placement |
| --- | --- | --- |
| Supplied site/building GLB scene | Three.js; rotation, zoom and camera-angle changes | Development 3D section. |
| Supplied panoramic JPEG points | Pannellum; looking around and configured transitions | Development panorama tour. |
| Supplied apartment GLB scene | Three.js; inspection of the selected supplied model | Apartment presentation and applicable finishing offer. |

The 3D and 360 controls are independent: one can exist without the other. Missing content hides the corresponding action. Base apartment presentation does not require an extra finishing record merely to attach ordinary supplied material.

Automatic model reconstruction and interior generation are excluded. Full collision-aware first-person building navigation is not required. Asset format support does not imply automatic conversion of plans into 3D.

## Validation and acceptance

Files belong to the correct company/object and are served according to visibility. Valid supplied scenes open with the specified controls; absent or invalid material does not leave a working-looking public action. A saved coordinate opens the corresponding location, developer corrections appear in the retained infrastructure view, and a parking enquiry reaches the correct company.

[[jobs]] owns file lifecycle, [[data]] owns relationships, and [[navigation]] owns screen placement.
