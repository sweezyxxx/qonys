# Project management and risks

The management baseline dated 24 October 2026 defines team responsibilities, work packages, review rules, milestones and dependencies for implementation.

## Ownership and review

Temirlan Almukhamedov is the Systems Analyst and Technical Coordinator. He is responsible for requirements, system/data models, architecture, documentation, repository/environment coordination and traceability. Yevgeniy Averyanov owns backend implementation. Bexultan Nishanbek owns Flutter Web/frontend implementation. Joint review of database models and API contracts is assigned to all three team members. Islam Omirzak is the project supervisor.

The agreed contribution policy uses individual Git identities and review of each meaningful change against its requirement and acceptance criteria. Responsibility for documentation and coordination is separate from implementation authorship. Requirement references connect versioned documents, project summaries and tracker tasks.

## Milestones

| Milestone | Target | Completion evidence | Dependency |
| --- | --- | --- | --- |
| M0 Analysis and design review | 24 October 2026 | Proposal, user research, comparisons, requirements, three diagrams, key-scenario mockups, evaluation and management plans, and review records. | Scope and requirement baseline. |
| M1 Data and access foundation | After M0 | Reviewed entity/API contracts; runnable ownership/account/draft flow; initial model feasibility notes on actual resources. | Confirmed baseline and configured development environment. |
| M2 Buyer and developer vertical path | After M1 | A development is completed and published; buyer reaches a physical apartment and submits a correctly owned enquiry. | M1; required content and valid linked regions. |
| M3 Assisted selection and visual content | Alongside M2 after feasibility checks | Local multilingual preference interpretation, corrected region suggestions and supplied optional viewers demonstrated with actual inputs. | Early feasibility work; validated visual input materials. |
| M4 Verification and final preparation | After integrated scenarios | Small actual scenario records, documented defects/fixes, supervisor review and a tagged deliverable version. | Runnable features; real review and contribution records. |

The sequence identifies dependencies between deliverables. Model feasibility checks run alongside the data foundation so that resource constraints can inform integration decisions early.

## Work package allocation

| Local planning ID | Outcome | Accountable owner | Review and acceptance |
| --- | --- | --- | --- |
| WP-01 | Scope, requirements and architectural/data contracts | Temirlan | Both developers review feasibility and consistency; decisions link to affected requirements. |
| WP-02 | Accounts, ownership and catalogue API | Yevgeniy | Frontend verifies contract use; access checks distinguish own, unrelated and public/draft records. |
| WP-03 | Responsive catalogue, development, floor and apartment path | Bexultan | Correct physical record, availability and selected finishing reach the enquiry path. |
| WP-04 | Gradual developer content and publication validation | Yevgeniy and Bexultan | Incomplete drafts persist; the approved mandatory minimum gates first publication; later valid saves are immediately public. |
| WP-05 | Correctable facade/floor image regions | Bexultan for editor; Yevgeniy for processing integration | Geometry and record-link checks are separate; manual preparation remains possible. |
| WP-06 | Local buyer selection and language handling | Yevgeniy for backend; Bexultan for dialogue; Temirlan for cases | Real returned IDs satisfy hard constraints; no unconfirmed relaxation; language checked with paired examples. |
| WP-07 | Enquiries, SMTP and administration | Yevgeniy and Bexultan | Enquiry persists independently of mail delivery; ownership, moderation reason/restoration and key audit events behave as required. |
| WP-08 | Verification and submission evidence | Temirlan coordinating all members | Actual results, reviews and limitations are attached to the relevant real issue/version. |

The defined task policy requires one accountable assignee, requirement references, an expected outcome, acceptance criteria and a due date for each YouTrack task. WP identifiers group the planned work; tracker keys identify individual tasks and their review records.

## Risk register

The register links technical and delivery risks to concrete mitigation actions and responsible team members.

| Risk | Consequence | Planned response | Owner |
| --- | --- | --- | --- |
| Local model does not fit available resources | Slow or unavailable dialogue during the demonstration. | Run an early small checkpoint trial; record actual resources and latency; retain ordinary catalogue filtering while resolving model fit. | Yevgeniy; Temirlan coordinates scope review. |
| Russian, Kazakh and English interpretation differs | Wrong hard constraints or unsupported explanations. | Use paired meanings, inspect extracted fields and actual stock; clarify ambiguity and validate server-side. | Temirlan and Yevgeniy. |
| Generic masks fragment apartments or confuse facade features | Incorrect regions or excessive editing. | Evaluate the two tasks separately; support manual editing/drawing and explicit reviewed record assignment. | Yevgeniy and Bexultan. |
| Visual input quality or format varies | Region processing or viewers may need additional preparation. | Validate inputs early, use representative examples and retain manual region preparation. | Temirlan. |
| Stale price/status or optional offer changes | An enquiry could carry misleading current information. | Revalidate at submission, require price confirmation, reject unavailable stock and retain historical snapshots. | Yevgeniy. |
| Draft/other-company data leaks | Incorrect public visibility or unauthorised editing. | Centralise ownership/visibility rules and check direct URLs, files, AI search and worker operations. | Yevgeniy. |
| Map/source coverage or SMTP delivery is unreliable | Incomplete infrastructure context or missing email notification. | Keep approved infrastructure records/corrections and inbox records independent of provider availability; inspect the failure path. | Yevgeniy and Bexultan. |
| Submission records lose traceability | A reviewer may be unable to connect a report version to its sources and contributions. | Keep interview notes, review comments, tracker references and tagged versions together; verify reviewer access before submission. | Temirlan and all contributors. |

## Project coordination and version control

The project links are the [GitHub repository](https://github.com/sweezyxxx/qonys), [YouTrack workspace](https://qonys.youtrack.cloud/) and [Notion workspace](https://app.notion.com/p/402878b53f0980a9bebafc8ef6d32613). They serve version control, task tracking and project knowledge respectively.

The 24 October submission form requires the tag `prob-period-1` on the exact submitted commit. Later stages use their announced tag conventions. Task branches and pull requests link changes to requirements and another team member's review. Each YouTrack task records its assignee, priority, outcome, acceptance criteria and deadline. The submission record identifies the revision, completed work, limitations, outstanding tasks and reviewer access.

## Recorded stage contributions

| Team member | Completed work | Repository evidence |
| --- | --- | --- |
| Temirlan Almukhamedov | Requirements, architecture/data design, report, research synthesis, prototype, living documentation and repository workflow. | QON-3/QON-4; merged [PR 2](https://github.com/sweezyxxx/qonys/pull/2) and [PR 3](https://github.com/sweezyxxx/qonys/pull/3). |
| Yevgeniy Averyanov | Django backend initialization. | QON-1; [commit 0b317ef](https://github.com/sweezyxxx/qonys/commit/0b317ef7d8cea5df761477b135c0191be7a217ce). |
| Bexultan Nishanbek | Flutter client initialization, counter screen, widget-test source and web/platform runners. | QON-2; [commit 29e9e1b](https://github.com/sweezyxxx/qonys/commit/29e9e1b), merged [PR 4](https://github.com/sweezyxxx/qonys/pull/4). |

The current code provides application scaffolds. The business workflows and client/backend integration follow the analysis/design baseline. QON-5 and QON-6 track prototype and architecture reviews; QON-7 tracks final submission evidence, access and the tagged revision.
