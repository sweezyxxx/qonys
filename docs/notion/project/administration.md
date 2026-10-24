# Administration and Audit

The administrator manages developer admission, access restrictions, development moderation, reference data and key-change history. Developers continue to prepare and publish their own reviewed content.

Requirements: FR-03, FR-36–FR-40 and NFR-01. See [[requirements]].

## Developer access

Manual verification precedes company-account creation. One account is issued per company with emailed password activation and recovery. Suspension blocks developer access and hides the company's public developments while preserving content and enquiries.

Reactivation restores an otherwise valid development hidden only by company suspension. An individually hidden development remains restricted, and an unpublished draft remains private. Account reactivation is not first publication.

## Development moderation

Hiding requires a reason visible to the owner in the development workspace. Public lists, maps, AI retrieval, direct details and files respect the restriction. Ordinary saves or worker completion cannot clear it. After correction, the administrator controls restoration separately from the developer's content save.

## Reference data

Administrators can edit cities and finishing types. A referenced value cannot be deleted. Deactivation prevents new assignment while preserving its display and search access on existing records. This protects property identity and historical context.

## Overview

The overview presents developer, buyer, published-development and hidden-development counts. The following counting convention gives the implementation and verification one definition: developer count covers company records including suspended companies; buyer count covers registered buyer identities including unverified registrations; published-development count covers currently public developments; hidden-development count covers previously published developments restricted by company or individual moderation. Private drafts enter neither development count.

The counts are summaries and do not introduce buyer blocking or a buyer-management workflow.

## Audit history

Successful developer suspension/reactivation, development hiding/restoration and apartment price/availability changes create an attributed event with object, timestamp and relevant change values. The administrator can view and filter these events. Ordinary users cannot edit history; a general rollback feature is not defined.

Audit payloads exclude passwords, authentication/reset tokens and unnecessary enquiry contact data. Failed operations do not appear as successful domain changes.

## Acceptance

With public A, individually hidden B and private draft C, suspension hides A; reactivation restores eligible A, keeps B hidden and leaves C private. A hide without a reason is rejected. A saved edit cannot restore hidden content. Referenced city deletion fails; deactivation preserves existing display/search. Counts and audit events match the controlled records.

See [[states]], [[roles]] and [[verification]].
