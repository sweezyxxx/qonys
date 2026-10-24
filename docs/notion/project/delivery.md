# Responsibilities and Delivery Workflow

## Ownership

| Team member | Role | Responsibilities |
| --- | --- | --- |
| Temirlan Almukhamedov | Systems Analyst and Technical Coordinator | Requirements, scenarios/acceptance, architecture and data modelling, documentation, database design with backend, repository/environment coordination and verification traceability. |
| Yevgeniy Averyanov | Backend Developer | Domain implementation, API, authentication/permissions, database migrations, persistence, workers, email and provider integrations. |
| Bexultan Nishanbek | Flutter Web Developer | Responsive client, screen flows, region editor, maps/viewers, comparison/assistant interaction and API integration. |

Islam Omirzak is the supervisor. Architecture, database models and API contracts receive joint team review. Coordination ownership does not replace another member's implementation authorship.

## Work sequence

The implementation sequence follows dependencies: data/access foundation → buyer/developer path → assisted selection and visual integration → verification and review. Model resource trials run alongside the foundation so feasibility informs integration early. [[decisions]] contains the technical risks.

| Work package | Main ownership | Verifiable outcome |
| --- | --- | --- |
| Data/access foundation | Yevgeniy, with Temirlan on model/contracts | Roles, owned records, account flows and private draft persistence. |
| Buyer navigation | Bexultan and Yevgeniy | Correct physical unit and offer from catalogue to enquiry. |
| Content/publication | Both developers, Temirlan on criteria | Complete first release, reviewed links and immediate valid later saves. |
| Region preparation | Bexultan on editor; Yevgeniy on processing | Correctable candidates and valid record associations. |
| Buyer AI | Yevgeniy on interpretation/search; Bexultan on UI; Temirlan on cases | Catalogue-grounded multilingual selection with confirmed relaxation. |
| Enquiries/administration | Both developers | Durable snapshots/inbox, processing, restrictions, reference protection and audit. |
| Verification/documentation | Temirlan coordinating all members | Actual scenario results, resolved defects and traceable reviewed changes. |

## Task and Git workflow

YouTrack is the task system. Each meaningful task identifies one accountable assignee, priority, expected outcome, requirement IDs, acceptance criteria and deadline. A change links back to its real task; the task links to the resulting commit or pull request and verification evidence.

Each member uses their own Git identity. Task branches and pull requests preserve review before merging to the shared main baseline. The 24 October 2026 form requires the tag `prob-period-1` on the exact submitted revision; later stages use their announced tags. Created documents, planned tasks and implementation completion are recorded according to the evidence available.

## Change and completion policy

A change identifies affected rules, modules, data relationships, interfaces and verification cases. The requirement matrix and owning module page are updated together. A task is complete only when its acceptance criteria are met and the change has the appropriate review/evidence; a status or page count does not establish completion.

Notion holds the current project specification. Git retains versioned artifacts and source. The separate [[defence]] branch retains the milestone report, research, interviews and submission files. Subsequent working-document changes do not silently rewrite that submission snapshot.

[GitHub repository](https://github.com/sweezyxxx/qonys) · [YouTrack workspace](https://qonys.youtrack.cloud/)

## Current stage record — 24 October 2026

The analysis/design package and completed README were merged through [PR 2](https://github.com/sweezyxxx/qonys/pull/2) and [PR 3](https://github.com/sweezyxxx/qonys/pull/3). Bexultan's Flutter initialization was merged through [PR 4](https://github.com/sweezyxxx/qonys/pull/4). All three members now have identifiable repository contributions.

| Task | Owner | Current outcome |
| --- | --- | --- |
| [QON-1](https://qonys.youtrack.cloud/issue/QON-1) | Yevgeniy | Django scaffold, commit 0b317ef. |
| [QON-2](https://qonys.youtrack.cloud/issue/QON-2) | Bexultan | Flutter counter scaffold, widget-test source and runners, commit 29e9e1b and merged PR 4. |
| [QON-3](https://qonys.youtrack.cloud/issue/QON-3) | Temirlan | README and repository workflow, merged PRs 2 and 3. |
| [QON-4](https://qonys.youtrack.cloud/issue/QON-4) | Temirlan | Versioned report, diagrams, research, prototype and living specification, merged PR 2. |
| [QON-5](https://qonys.youtrack.cloud/issue/QON-5) | Bexultan | Actual prototype/workflow review remains open. |
| [QON-6](https://qonys.youtrack.cloud/issue/QON-6) | Yevgeniy | Actual architecture/data/contracts and setup review remains open. |
| [QON-7](https://qonys.youtrack.cloud/issue/QON-7) | Temirlan | Supervisor statement recorded; reviewer access, final reviewed update, screenshots and submission tag remain. |

Islam Omirzak's written feedback was received on 24 October and is retained verbatim in [section 11 of the milestone report](https://app.notion.com/p/403878b53f098141b165f037b9e8debb). The approved scope and requirements remain unchanged.

Backend system/migration checks passed. The Flutter dependency check stopped because local Dart 3.12.2 does not satisfy the client's declared `^3.13.5`; analysis, tests and a web build require a compatible SDK. Prototype inspection covers local design interactions rather than integrated application acceptance. No submitted GitHub review was recorded on PRs 2–4 when inspected.

The submission owner must verify supervisor/committee access, complete review records and create `prob-period-1` on the final commit. One representative submits the form by 18:00 on 24 October, including the task-board/individual-task screenshots combined into one PDF of at most 10 MB. Each member's academic group and exact GitHub profile must be included.

[Versioned delivery evidence](https://github.com/sweezyxxx/qonys/blob/main/docs/delivery/2026-10-24.md) records contributions, checks and remaining actions.
