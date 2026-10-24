# Image Region Preparation

This module prepares selectable regions on developer-supplied images. A facade task proposes visible floor regions; a floor-plan task proposes apartment regions. SAM 2/OpenCV and project-specific processing provide candidates that the developer can correct and link to records.

Requirements: FR-07/FR-08, FR-21, FR-27/FR-28 and NFR-02/NFR-06. See [[requirements]].

## Inputs and outputs

| Task | Input context | Reviewed output |
| --- | --- | --- |
| Facade preparation | Owned building image and its declared floors | Editable regions linked to floors in that building. |
| Floor-plan preparation | Owned floor plan and its physical apartment records | Editable regions linked to apartments on that floor. |

A facade does not reveal an internal floor plan. Generic masks may cover rooms, furniture or facade details rather than complete apartments/floors. Region geometry and catalogue identity are therefore checked separately.

## Developer workflow

1. Save an image against the owned building or floor.
2. Request candidate preparation and inspect its progress/result.
3. Move, add, remove or replace boundaries as needed.
4. Assign the correct owned floor/apartment to each region.
5. Review and save the mappings.

Manual drawing and correction remain available when suggestions are unsuitable or a processing task fails. Candidate generation does not infer apartment prices, numbers or availability. Unreviewed candidates do not become public.

## Repeated floors

The developer may copy a prepared plan and reviewed geometry to matching floors. Target floors retain separate apartment identities, numbers, prices and availability. Copied associations are reviewed before publication; geometric similarity alone does not establish a valid target mapping.

## Persistence and visibility

The source asset, candidate geometry, reviewed geometry and target record links have distinct responsibilities. A worker result is not a publication action. Saving reviewed geometry on a private draft keeps it private; a valid reviewed save on a public development updates the public geometry immediately. Restrictions remain effective.

## Verification

Facade and floor-plan cases are evaluated separately against manual preparation on the same input. The record includes missing/extra/fragmented regions, geometry changes, final link correctness and correction effort. If timing is compared, it includes inference, waiting, correction and assignment at comparable final quality.

[[data]] defines mapping relationships; [[jobs]] defines processing and file handling; [[publication]] owns initial publication eligibility.
