# System Architecture

QONYS uses a modular Django/DRF application with shared PostgreSQL, a Flutter Web client, server filesystem storage and background workers. A worker process is part of the same application design rather than an independently owned domain service.

## Runtime responsibilities

| Component | Responsibility | Boundary |
| --- | --- | --- |
| Flutter Web | Screens, forms, comparison context, region editing, maps and embedded viewers | Uses the API; does not authorise domain changes by itself. |
| Django/DRF | Identity, ownership, catalogue operations, publication checks, selection orchestration, enquiries and administration | Owns validation and persistence decisions. |
| PostgreSQL | Structured business records, relations, commercial state, visibility, job/file metadata and enquiry snapshots | Binary assets remain in managed file storage. |
| Django storage on server filesystem | Managed uploads and generated geometry/assets | Private files require the same ownership/visibility checks as their objects. |
| RabbitMQ and Celery | Delivery and execution of background jobs | Workers reuse application domain and data-access rules. |
| Ollama/Qwen3 | Local interpretation of buyer preferences | Returns an interpretation, not authoritative stock or commercial data. |
| SAM 2/OpenCV processing | Candidate segmentation and project-specific geometry preparation | Developer correction and explicit record assignment establish reviewed mappings. |
| OSM sources and SMTP | External mapping/infrastructure inputs and outbound email | External failure does not rewrite domain truth or erase accepted enquiries. |

## Logical modules

Identity and companies, catalogue/content, buyer selection, region preparation, personal features, enquiries, and administration/audit have clear responsibilities inside one application. Cross-module changes use the relevant domain operation so that ownership, publication and commercial checks are applied consistently.

Three.js and Pannellum are embedded client-side viewers. Required image-based navigation works without optional models or panoramas.

## System context

{{CONTEXT_DIAGRAM}}

## Components

{{COMPONENT_DIAGRAM}}

## Design links

[[data]] defines the logical entities and their fields. [[states]] defines lifecycle and visibility rules. [[contracts]] defines application interactions and [[jobs]] covers worker/file responsibilities. [[decisions]] records the modular-monolith, storage, map, viewer and local-AI choices.

The rendered context, use-case and component figures in [[defence-architecture]] preserve the analysis-stage snapshot. The diagrams above provide editable semantic sources for the working architecture.
