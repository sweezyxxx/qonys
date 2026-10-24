# Accounts and Company Access

This module owns buyer registration and verification, sign-in, password recovery, administrator-created developer access and account preferences. Company content and enquiries remain owned by their respective modules.

Requirements: FR-01–FR-04, FR-14 and NFR-01/NFR-07. Full acceptance criteria are in [[requirements]].

## Buyer lifecycle

1. A visitor registers with email and password.
2. The registration email must be verified before buyer-account access is granted.
3. Until verification, the visitor retains public catalogue, assistant and comparison access.
4. A verified buyer can use Favourites, My enquiries and Account settings.
5. Email-based recovery permits a password reset without changing the account identity.

Favourite and enquiry operations enforce verification in the API as well as the interface. Opening a direct API operation cannot bypass the guest gate.

## Profile

Name, surname and phone are optional until an enquiry needs them. They can be edited in Account settings and prefilled into the enquiry form, where the buyer can correct them. Correcting an enquiry does not automatically rewrite previous enquiry snapshots or imply a profile update. Password changes are supported; the email is displayed without a first-version address-change workflow.

Guest comparison entries survive sign-in, including each physical apartment and selected finishing context. This does not introduce guest favourites or promise persistence across browser restarts.

## Developer lifecycle

The administrator manually verifies the representative and creates one account for the company. An activation email lets the representative set their own password. Password recovery also uses email. The representative then manages the company's content and enquiries within the access rules.

Developer suspension/reactivation is an administrative operation. It does not destroy the company, its drafts, publication history or accepted enquiries. Public company self-registration and additional employee accounts are excluded.

## Data and dependencies

User identity stores role, email, verification and password credentials. Company membership identifies the single developer account and its access state. Passwords and authentication tokens do not appear in public responses or audit payloads. SMTP handles verification, activation and recovery mail; notification failure is distinguished from the underlying account or enquiry record.

## Acceptance examples

- An unverified registration can browse but cannot enter Favourites or submit an enquiry.
- Signing in retains the guest comparison and selected finishing offers.
- Developer A cannot open Developer B's private file or inbox by changing an identifier.
- A suspended company cannot continue editing or expose its developments publicly.

Related rules: [[roles]], [[enquiries]], [[administration]] and [[jobs]].
