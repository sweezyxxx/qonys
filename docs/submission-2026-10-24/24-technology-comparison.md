# Technology alternatives and selected decisions

Review date: 24 October 2026. Five technology decisions are compared against application consistency, integration effort, data ownership, resource needs and the selected interaction model. The assessment uses primary documentation and the scientific sources in the literature review.

## Application structure

| Alternative | Fit to the project | Cost or limitation |
| --- | --- | --- |
| Modular Django application with shared PostgreSQL | Keeps accounts, ownership, catalogue publication and enquiries within one application boundary. Background workers reuse domain rules. | Requires clear internal module interfaces; ownership checks are enforced within each module. |
| Independently deployed domain services | Permits separate domain deployment and service boundaries. | Adds network contracts, distributed failure handling and cross-service data coordination to a three-person project. These costs are not justified by demonstrated scale requirements. |

**Selected:** modular monolith (DEC-40). API and worker processes can run separately while retaining shared domain rules and persistence. This structure fits the team size and keeps account, catalogue and enquiry consistency within one application boundary.

## Backend API framework

| Alternative | Documented mechanism | Project assessment |
| --- | --- | --- |
| Django with Django REST Framework | Serialisation, authentication/permission policies and API views integrate with Django; [DRF documentation](https://www.django-rest-framework.org/). | Retains the confirmed stack and suits the related administrative, content and account workflows. Permissions still require explicit implementation and verification. |
| FastAPI | Typed request validation, OpenAPI documentation and dependency injection; [official feature description](https://fastapi.tiangolo.com/features/). | A credible Python API alternative, but changing the baseline would require reworking integration choices without an identified requirement requiring that change. |

**Selected:** Django/DRF. Its application structure fits the chosen modular architecture and the team roles. Dependency pinning and review are part of the environment acceptance criteria.

## Uploaded asset storage

| Alternative | Fit | Trade-off |
| --- | --- | --- |
| Dedicated server filesystem through Django storage | A documented built-in backend stores uploaded assets; ownership and metadata remain in the database. | Avoids an additional storage service for the initial deployment; file backup and access controls remain necessary. |
| Separate object storage through a storage backend | Separates asset storage from the application host. | Adds a storage service, access-policy configuration and operational dependencies to the prototype. |
| Database large objects | PostgreSQL provides streamed large-object access. | Combines binary lifecycle with database operations and backups. The prototype has no demonstrated need to put large visual assets inside PostgreSQL. |

**Selected:** filesystem storage under DEC-41, with metadata and ownership in PostgreSQL. [Django storage API](https://docs.djangoproject.com/en/5.2/ref/files/storage/) defines the backend abstraction; [PostgreSQL large objects](https://www.postgresql.org/docs/current/largeobjects.html) establishes the third alternative. Private draft files are retrieved through an authorised application path, with ownership checks independent of file location.

## Buyer preference interpretation

| Alternative | Fit | Trade-off |
| --- | --- | --- |
| Local Qwen3 with Ollama structured output | Approved initial approach for multilingual preference extraction, followed by backend validation and catalogue filtering. | Resource fit and interpretation quality must be checked on the selected checkpoint. Valid JSON can still encode misunderstood preferences. |
| Local Llama-family interpreter | A research alternative supported by the multilingual model report. | The exact artifact, licence conditions, required languages and hardware fit need separate checking; it is not an approved replacement. |
| Rules and structured filters | Deterministic handling of explicitly entered fields; useful as the manual baseline and ordinary catalogue flow. | Free-text phrasing, synonyms and conversational refinement require more handcrafted interpretation. It cannot be assumed equivalent to the approved natural-language experience. |

**Selected:** Qwen3/Ollama (DEC-53), with deterministic business validation and actual-stock retrieval. Sources S1–S4 and T1 in the literature review explain the distinction between interaction, model capabilities and response format. The choice avoids paid inference APIs. Computing resources and multilingual interpretation are assessed under the evaluation plan.

## Image region suggestions

| Alternative | Fit | Trade-off |
| --- | --- | --- |
| SAM 2 plus OpenCV and project-specific processing | Prompted masks can be processed into editable contour suggestions and reviewed by the developer. | Complete apartment/floor semantics, grouping and record links remain QONYS research tasks. Generic masks are not sufficient proof of correctness. |
| Classical OpenCV processing with manual regions | Useful for clean contours and the simplest manual baseline. | Text, furniture, weak boundaries and drawing styles can interfere with heuristics; domain robustness is unmeasured. |
| Specialised floor-plan vectorisation model | CubiCasa5K-related methods and Raster2Seq address architectural semantics or structured polygons. | Their output categories differ from facade floors and saleable apartment identities. Adapting them would add evaluation and integration work; no replacement is selected. |

**Selected:** the SAM 2/OpenCV research approach with manual correction and record assignment (DEC-54). Scientific sources S5–S9 explain why segmentation, architectural structure and stock identity require separate treatment. The [SAM 2 repository](https://github.com/facebookresearch/sam2) documents the implementation, and the [OpenCV licence page](https://opencv.org/license/) supplies licence context. The initial evaluation compares suggested and corrected regions with manual preparation on the same inputs.

## Consequences for implementation

The comparisons support a single coherent implementation boundary: Flutter Web calls the Django API; PostgreSQL holds business data and file metadata; the approved filesystem backend holds assets; Celery/RabbitMQ execute slow processing; local AI is invoked through defined application interfaces. File and catalogue access rules apply equally to ordinary screens, AI results, copied floor mappings and background tasks. Optional GLB/Three.js and JPEG/Pannellum viewers remain the selected visualisation choices for optional supplied assets.

The five decisions each compare two or three alternatives against the agreed scope, integration requirements and expected implementation effort.
