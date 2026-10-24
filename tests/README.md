# Verification entry points

## Documentation and stage artifacts

Run `python scripts/check_documentation.py` from the repository root. It checks the curated bundle: the fixed title/team order, all 50 requirement rows with priorities and acceptance text, functional ownership, internal wiki references, referenced local files, checked report/transcript hashes, editable diagrams and prototype exports. It uses the Python standard library.

Run `python scripts/build_project_documentation.py` to regenerate the 29 native Notion page payloads from committed sources. Output goes to ignored `work/notion-migration/`; this command does not change Notion.

The report and prototype verification records under `docs/submission-2026-10-24/` identify earlier actual inspections and their scope. They do not prove a Flutter/Django integration or real AI behaviour. Document checking follows the stakeholder's text-only instruction.

To repeat local prototype interaction checks, install Node.js and `npm install --no-save playwright@1.62.1`, then install Chromium with `npx playwright install chromium` and run `node scripts/inspect_submission_prototype.mjs`. Alternatively set `CHROMIUM_PATH` to an already installed Chromium/Edge executable. By default the script generates no screenshots and writes a new result under ignored `work/verification/`. Explicit `--screenshots` refreshes screen exports and creates a new inspection record beside the prototype.

## Existing backend

Follow [backend setup](../backend/README.md), then run Django `check` and `makemigrations --check --dry-run`. Record the interpreter/dependency versions and any failures. Default Django consistency checks are not project business tests.

## Application acceptance during implementation

The [evaluation plan](../docs/submission-2026-10-24/17-evaluation-plan.md) defines six workflow cases and six small multilingual AI cases, comparison conditions and per-case records. Add executable checks with the corresponding feature when it exists. Ownership isolation, visibility restrictions, availability changes and enquiry price confirmation require server-side tests; a local mockup cannot establish those controls.
