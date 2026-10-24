# Contribution and review workflow

Each member commits through their own account and Git identity. Preserve existing authorship; report preparation does not create another member's implementation contribution.

1. Open or update the actual YouTrack task with one assignee, priority, expected outcome, affected requirement IDs, acceptance criteria and deadline.
2. Create a task branch, for example `codex/QON-3-submission-documentation` or `feature/QON-2-flutter-init`.
3. Make meaningful commits with the issue ID, for example `QON-3: Document backend setup and repository workflow`.
4. Open a pull request linking the task. Explain the resulting change and actual checks, including any checks that could not run.
5. Have another team member review it. Resolve material feedback before merging. Link the resulting PR/commit and verification evidence back to YouTrack.
6. Update the affected living module, requirement and shared contract when behaviour changes. Preserve the dated defence snapshot separately.

Use `pre-defense-1`, `pre-defense-2` and `final-pre-defense` as the respective stage tags. Apply a tag to the exact reviewed submission commit and record its commit URL in the delivery record. Do not move an existing submitted tag silently or tag a version as reviewed before actual review.

The submission owner verifies team, supervisor and committee access to the private repository and documentation. Do not change repository visibility as a substitute for granting the intended readers access.

Real credentials, personal local environments, databases, uploads, runtime downloads and working caches stay outside Git. Environment examples contain placeholders. Do not invent historical commits, approval records, supervisor comments or test measurements.
