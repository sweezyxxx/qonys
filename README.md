# QONYS

**Development of an AI-Powered Residential Real Estate Visualization and Intelligent Property Selection Platform with 3D Site Visualization, Floor-Level Layouts, and Interactive Mapping**

QONYS helps buyers find and compare individual new-build apartments across developers. It connects available stock and prices to buildings, floors, apartment plans and infrastructure, with optional supplied 3D assets and a multilingual selection assistant. Developers maintain their own stock and content; administrators manage verified company access and publication restrictions.

## Problem and target users

Choosing a new-build apartment requires matching price, availability, finishing, location and layout information for a specific physical unit. Separate listings, plans and developer materials make that comparison difficult and can leave a buyer uncertain about which apartment and offer they are viewing. Developers also need a consistent way to keep stock, prices and linked visual materials current.

QONYS addresses this problem through a shared catalogue with a stable apartment identity, linked spatial navigation and catalogue-grounded selection. Its target users are:

- **Buyers:** people searching for an apartment for their own use or rental investment who need to shortlist, compare and enquire about actual units.
- **Developer representatives:** verified companies maintaining their developments, apartment stock, prices, finishing offers and incoming enquiries.
- **Administrators:** platform operators verifying developer access, managing shared reference data and enforcing publication restrictions.

## Project links

- [Working project documentation in Notion](https://app.notion.com/p/402878b53f0980a9bebafc8ef6d32613)
- [24 October submission in Notion — defence24.10.26](https://app.notion.com/p/403878b53f09815793b1d6ba8d168cbf)
- [YouTrack project](https://qonys.youtrack.cloud/issues/QON)
- [Versioned documentation index](docs/README.md)
- [English stage report and sources](docs/submission-2026-10-24/README.md)
- [Stage delivery record and remaining reviews](docs/delivery/2026-10-24.md)

## Team

| Member | Role | Responsibilities |
| --- | --- | --- |
| Temirlan Almukhamedov | Systems Analyst and Technical Coordinator | Gather and maintain requirements; define workflows and acceptance criteria; coordinate architecture and database design, documentation, repository/environment setup and verification traceability. |
| Yevgeniy Averyanov | Backend Developer | Implement domain models, database migrations, API contracts, account and ownership controls, persistence, background processing, email and provider integrations. |
| Bexultan Nishanbek | Flutter Web Developer | Implement responsive screens and navigation, apartment comparison and assistant interactions, region editing, maps/viewers and client integration with the backend. |

Supervisor: **Islam Omirzak**.

## Scope

The intended application provides a city catalogue, maps and linked building/floor/apartment navigation; four-apartment comparison; developer-configured base finishing and optional priced offers; verified buyer accounts and enquiries; gradual private content preparation and complete first publication; manual correction of image regions; and developer/admin workspaces. Interface content and buyer selection support Russian, Kazakh and English.

Guests can browse, compare and use selection. Favourites and enquiries require verified email sign-in. Each catalogue card represents one physical apartment. An enquiry preserves the confirmed apartment, finishing and price context; it does not reserve stock or collect payment.

Developer chatbots, interior design generation, question answering over developer documents, automatic 3D reconstruction, payments and automatic apartment reservation are outside the approved scope. The complete [requirement matrix](docs/notion/project/requirements.md) defines 40 functional and 10 non-functional requirements with priorities and acceptance criteria.

## Expected outcomes

The intended project outcomes are:

1. A web application in which buyers can move from a city catalogue and linked plans to a specific apartment, compare up to four units and submit an enquiry with confirmed finishing and price context.
2. A developer workspace for gradual private content preparation, complete first publication, stock and offer updates, and enquiry processing, supported by administrative access and visibility controls.
3. Russian, Kazakh and English property selection grounded in actual published stock, with validated search constraints and human-correctable image regions.
4. A traceable engineering package connecting the implementation to requirements, editable diagrams, project tasks and lightweight workflow/selection evaluation results.

These outcomes define the implementation target. The current analysis/design deliverables and existing code are identified below.

## Current state

The analysis/design package contains the English report, three supplied interview transcripts with traceable findings, literature and system/technology comparisons, editable architecture diagrams, and an interactive HTML design prototype with nine screen exports. The working Notion specification has seven sections and 22 topic pages.

The existing backend is a Django project scaffold from [QON-1](https://qonys.youtrack.cloud/issue/QON-1). It currently uses SQLite and console email with the default Django applications and admin route. Business models, the API, buyer/developer account flows, SMTP, workers and AI integrations are planned. Bexultan Nishanbek ([RealCart](https://github.com/RealCart)) completed [QON-2](https://qonys.youtrack.cloud/issue/QON-2): the Flutter application scaffold in `qonys_app/` was merged through [PR 4](https://github.com/sweezyxxx/qonys/pull/4). It contains the standard counter screen, a widget smoke test and web/platform runner files. The buyer/developer screens and backend integration are the next implementation work. Prototype interactions use fictional local data and a scripted assistant.

The 24 October stage requires analysis, design and key-scenario mockups. A complete application is not a stated minimum for this stage. Actual review and access requirements are tracked in the [delivery record](docs/delivery/2026-10-24.md).

## Selected architecture

The target is Flutter Web with a modular Django/DRF backend and PostgreSQL, Celery/RabbitMQ processing, server-side file storage, OpenStreetMap, optional Three.js/Pannellum viewers, and free local Qwen/Ollama preference interpretation. SAM 2/OpenCV region proposals require grouping and human correction. These are design choices, not installed features of the scaffold. The backend's existing Python and dependency versions are defined by `backend/pyproject.toml` and `backend/uv.lock`.

## Repository layout

```text
backend/                      Existing Django scaffold and setup instructions
qonys_app/                    Flutter scaffold, widget test and web runner
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

### Prerequisites and repository setup

- Git and a GitHub account with access to this private repository.
- A modern browser for the local prototype and Flutter Web.
- Flutter with a bundled Dart SDK satisfying `^3.13.5`, as declared in `qonys_app/pubspec.yaml`. Check `flutter --version` before resolving client dependencies.
- [uv](https://docs.astral.sh/uv/getting-started/installation/) for the backend; its project requires Python 3.14 or later, which uv can obtain as a managed interpreter.
- Python 3.12 or later for the standalone documentation-check commands below.

```console
git clone https://github.com/sweezyxxx/qonys.git
cd qonys
```

### Design prototype

After cloning or extracting the repository, open the local [prototype HTML file](docs/submission-2026-10-24/prototype/index.html) in a browser. It runs without an application server or external account. The GitHub file view displays its source; the interactive version is the local file. It uses fictional data and local scripted interactions.

### Django scaffold

From the repository root:

```console
cd backend
uv sync --frozen
```

For the first local setup, copy `.env.example` to `.env` inside `backend/`. Generate a local secret key with the following command, run from `backend/`, and replace the placeholder in `.env` with its output:

```console
uv run python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Keep `.env` local. `DJANGO_DEBUG=True` is the local development setting; console email does not require SMTP credentials. Start the existing scaffold from `backend/`:

```console
uv run python manage.py check
uv run python manage.py migrate
uv run python manage.py runserver 127.0.0.1:8000
```

The existing route is `http://127.0.0.1:8000/admin/`; the scaffold does not yet serve the buyer/developer application. [Backend setup](backend/README.md) explains local admin-user creation and additional details. Stop the server with Ctrl+C.

### Flutter Web scaffold

From the repository root, using a compatible Flutter/Dart SDK:

```console
cd qonys_app
flutter pub get
flutter run -d chrome
```

The current screen is the initialization counter example. [Client setup and checks](qonys_app/README.md) describes its contents. The local documentation check used Flutter 3.44.2 with Dart 3.12.2; `flutter pub get` stopped because this Dart version does not satisfy the declared constraint. Client analysis, tests and a web build must be run with a compatible SDK; see the [recorded result](docs/delivery/verification/frontend-scaffold.json).

### Verification commands

From `backend/`:

```console
uv run python manage.py check
uv run python manage.py makemigrations --check --dry-run
uv run python manage.py test
```

The first two commands check Django configuration and migration consistency. The current scaffold has no project-specific business tests; a zero-test run does not establish application acceptance. The [evaluation plan](docs/submission-2026-10-24/17-evaluation-plan.md) defines the planned workflow and multilingual selection checks.

From `qonys_app/`, after successful dependency resolution:

```console
flutter analyze
flutter test
flutter build web
```

The existing widget test covers the counter example. Application workflow acceptance follows the implemented business features.

Return to the repository root (`cd ..` if you are in `backend/` or `qonys_app/`) and check the documentation bundle without installing application dependencies:

```console
python scripts/check_documentation.py
python scripts/build_project_documentation.py
```

The second command builds local Notion payloads without publishing. To rebuild the Word report, run:

```console
python -m pip install -r scripts/requirements-docs.txt
python scripts/build_submission_report.py
```

Rebuilding changes the file hash and requires renewed text/pagination verification; the committed verification record identifies the checked report version.

See [verification entry points](tests/README.md) and [contribution workflow](CONTRIBUTING.md) for task links, review and stage tags.
