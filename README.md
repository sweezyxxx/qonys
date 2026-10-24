# QONYS

**Development of an AI-Powered Residential Real Estate Visualization and Intelligent Property Selection Platform with 3D Site Visualization, Floor-Level Layouts, and Interactive Mapping**

QONYS helps buyers find and compare individual new-build apartments across developers. It connects available stock and prices to buildings, floors, apartment plans and infrastructure, with optional supplied 3D assets and a multilingual selection assistant. Developers maintain their own stock and content; administrators manage verified company access and publication restrictions.

## Project links

- [Working project documentation in Notion](https://app.notion.com/p/402878b53f0980a9bebafc8ef6d32613)
- [24 October submission in Notion — defence24.10.26](https://app.notion.com/p/403878b53f09815793b1d6ba8d168cbf)
- [YouTrack project](https://qonys.youtrack.cloud/issues/QON)
- [Stage delivery record and remaining reviews](docs/delivery/2026-10-24.md)

## Team

| Member | Role |
| --- | --- |
| Temirlan Almukhamedov | Systems Analyst and Technical Coordinator |
| Yevgeniy Averyanov | Backend Developer |
| Bexultan Nishanbek | Flutter Web Developer |

Supervisor: **Islam Omirzak**.

## Scope and intended outcomes

The intended application provides a city catalogue, maps and linked building/floor/apartment navigation; four-apartment comparison; developer-configured base finishing and optional priced offers; verified buyer accounts and enquiries; gradual private content preparation and complete first publication; manual correction of image regions; and developer/admin workspaces. Interface content and buyer selection support Russian, Kazakh and English.

Guests can browse, compare and use selection. Favourites and enquiries require verified email sign-in. Each catalogue card represents one physical apartment. An enquiry preserves the confirmed apartment, finishing and price context; it does not reserve stock or collect payment.

Developer chatbots, interior design generation, question answering over developer documents, automatic 3D reconstruction, payments and automatic apartment reservation are outside the approved scope. The complete [requirement matrix](docs/notion/project/requirements.md) defines 40 functional and 10 non-functional requirements with priorities and acceptance criteria.

## Current state

The analysis/design package contains the English report, three supplied interview transcripts with traceable findings, literature and system/technology comparisons, editable architecture diagrams, and an interactive HTML design prototype with nine screen exports. The working Notion specification has seven sections and 22 topic pages.

The existing backend is a Django project scaffold from [QON-1](https://qonys.youtrack.cloud/issue/QON-1). It currently uses SQLite and console email with the default Django applications and admin route. Business models, the API, buyer/developer account flows, SMTP, workers and AI integrations are planned. Flutter Web initialization is tracked in [QON-2](https://qonys.youtrack.cloud/issue/QON-2); no Flutter application is included in this revision. Prototype interactions use fictional local data and a scripted assistant.

The 24 October stage requires analysis, design and key-scenario mockups. A complete application is not a stated minimum for this stage. Actual review and access requirements are tracked in the [delivery record](docs/delivery/2026-10-24.md).

## Selected architecture

The target is Flutter Web with a modular Django/DRF backend and PostgreSQL, Celery/RabbitMQ processing, server-side file storage, OpenStreetMap, optional Three.js/Pannellum viewers, and free local Qwen/Ollama preference interpretation. SAM 2/OpenCV region proposals require grouping and human correction. These are design choices, not installed features of the scaffold. The backend's existing Python and dependency versions are defined by `backend/pyproject.toml` and `backend/uv.lock`.

## Repository layout

```text
backend/                      Existing Django scaffold and setup instructions
docs/notion/project/          Living English specification sources and page manifest
docs/submission-2026-10-24/    Dated report, research and interview evidence
  diagrams/                   Editable diagram sources and readable exports
  prototype/                  Standalone HTML prototype and inspected screens
docs/delivery/                Tasks, verification, reviews and submission traceability
scripts/                      Documentation builders and bundle checks
tests/                        Verification entry points and planned application checks
.github/                      Pull request checklist
```

## Run and check

Open [the prototype](docs/submission-2026-10-24/prototype/index.html) in a browser. It runs without an application server or external account.

For the Django scaffold, follow [backend setup](backend/README.md). It uses uv, Python 3.14 or later, and the committed dependency lock. The environment example contains placeholders, never real credentials.

From the repository root, Python 3.12 or later can check the documentation bundle without installing application dependencies:

```console
python scripts/check_documentation.py
python scripts/build_project_documentation.py
```

The second command builds local Notion payloads without publishing. To rebuild the Word report, install `scripts/requirements-docs.txt` and run `python scripts/build_submission_report.py`. Rebuilding changes the file hash and requires renewed text/pagination verification; the committed verification record identifies the checked report version.

See [verification entry points](tests/README.md) and [contribution workflow](CONTRIBUTING.md) for task links, review and stage tags.
