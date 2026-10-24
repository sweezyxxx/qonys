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

## Current stage record — 24 October 2026

[Pull request 2](https://github.com/sweezyxxx/qonys/pull/2) contains the prepared analysis/design package on branch `QON-3-submission-documentation`. It is open and awaits an actual team review before merge. The existing backend initialization remains authored by Yevgeniy; current documentation commits are authored through Temirlan's account.

| Task | Accountable role | Current outcome |
| --- | --- | --- |
| [QON-1](https://qonys.youtrack.cloud/issue/QON-1) | Backend | Existing Django scaffold; commit 0b317ef. |
| [QON-2](https://qonys.youtrack.cloud/issue/QON-2) | Flutter Web | Initialization task exists; Flutter source is not present on the inspected main revision. |
| [QON-3](https://qonys.youtrack.cloud/issue/QON-3) | Coordination | README, setup and repository workflow in commit ee487bf; PR review pending. |
| [QON-4](https://qonys.youtrack.cloud/issue/QON-4) | Coordination | Versioned report, research, diagrams, prototype and living specification in commit 5f523a3; PR review pending. |
| [QON-5](https://qonys.youtrack.cloud/issue/QON-5) | Flutter Web | Actual prototype/workflow review remains open. |
| [QON-6](https://qonys.youtrack.cloud/issue/QON-6) | Backend | Actual architecture/data/contracts and setup review remains open. |
| [QON-7](https://qonys.youtrack.cloud/issue/QON-7) | Coordination | Supervisor comments, intended-reader access, reviewed release and stage tag remain open. |

The new stage task descriptions include a 24 October target, outcome, acceptance criteria and initial priority. Backend dependencies installed from the existing lock on Python 3.14.9; Django checks reported no issues and no migration changes. No project business tests exist yet. The documentation check passed 210 checks, the Notion payload builder generated 29 pages, and local prototype interaction/layout checks passed at 320, 736 and 1024 px without screenshots. These results do not establish application or AI acceptance.

No supervisor feedback has been received. The stakeholder deferred invitations for the supervisor and the remaining team member; access remains an explicit submission action. The checklist requires evidence of progressive repository contributions from every member, without specifying a code quota or commit count. Actual design/review findings and corrections can be committed by their author. Current task creation and document uploads do not reconstruct historical progression.

[Versioned delivery evidence](https://github.com/sweezyxxx/qonys/blob/QON-3-submission-documentation/docs/delivery/2026-10-24.md) identifies checks, outstanding reviews and the stage-tag sequence.
