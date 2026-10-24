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

Each member uses their own Git identity. Task branches and pull requests preserve review before merging to the shared main baseline. The stage tags pre-defense-1, pre-defense-2 and final-pre-defense identify the exact submitted revisions. Created documents, planned tasks and implementation completion are recorded according to the evidence available.

## Change and completion policy

A change identifies affected rules, modules, data relationships, interfaces and verification cases. The requirement matrix and owning module page are updated together. A task is complete only when its acceptance criteria are met and the change has the appropriate review/evidence; a status or page count does not establish completion.

Notion holds the current project specification. Git retains versioned artifacts and source. The separate [[defence]] branch retains the milestone report, research, interviews and submission files. Subsequent working-document changes do not silently rewrite that submission snapshot.

[GitHub repository](https://github.com/sweezyxxx/qonys) · [YouTrack workspace](https://qonys.youtrack.cloud/)
