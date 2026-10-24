# Background Jobs and File Lifecycle

Django accepts domain operations, RabbitMQ delivers work references, and Celery workers perform background processing using the same application rules. Slow processing does not keep a public update or enquiry request dependent on a long-running HTTP operation.

## Work types

| Work | Input/reference | Output and domain boundary |
| --- | --- | --- |
| Facade/floor-plan preparation | Stored owned image, task kind and target context | Candidate geometry and processing outcome; developer review establishes the saved mapping. |
| Enquiry notification | Accepted enquiry identity and intended company recipient | SMTP delivery outcome; the enquiry and snapshot already exist independently. |
| Account mail | Intended registration/activation/recovery context | Verification or account link delivery; no credentials in logs or public payloads. |

The logical processing lifecycle distinguishes waiting, running, completed and failed work. These are processing concepts rather than publication, stock or enquiry-processing states. UI progress and errors appear next to the affected image/task. Exact retry and scheduling parameters belong to deployment configuration.

## File lifecycle

1. An authorised developer uploads a file against an owned object.
2. Django storage keeps its managed filesystem reference; PostgreSQL retains ownership and metadata.
3. Validation and processing use the stored reference instead of trusting arbitrary client file locations.
4. Candidate geometry is retained as processing output, separate from reviewed saved associations.
5. Public serving follows the development's visibility; private drafts use authorised access.

The approved visual profiles are supplied GLB scenes and panoramic JPEGs. Building images, floor plans, covers and example media retain their relevant object context. A supported format still needs a usable file and valid relationship before its public action is shown.

## Failure handling

A failed segmentation task leaves a manual preparation path. It does not publish partial content or remove a restriction. SMTP failure leaves accepted enquiries accessible in both buyer history and the owning inbox. Recovery uses the existing enquiry identity, avoiding a second domain record for an already accepted request.

File access checks apply to direct requests as well as screens. Suspended/hidden development content is not exposed through a previously saved media URL. Backup/restore covers managed assets together with their database metadata so that references and ownership remain meaningful.

## Configuration responsibilities

The runtime requires database connectivity, RabbitMQ/worker configuration, managed storage paths and permissions, SMTP delivery configuration, local model/runtime artifacts and map/source integration settings. Secrets remain outside versioned documents; configuration examples use placeholders. Model digests, dependencies and resource profiles are recorded for reproducible verification.

[[architecture]], [[regions]], [[visuals]] and [[enquiries]] define the related application behaviour.
