# Roles and Access Matrix

QONYS distinguishes public visitors, verified buyers, property developers and platform administrators. Developer operations are restricted to the owning company; account role alone never grants access to another company's private data.

| Operation | Visitor or unverified registrant | Verified buyer | Active developer | Administrator |
| --- | --- | --- | --- | --- |
| Browse public stock, maps and apartment details | Yes | Yes | Public view | Public view |
| Use buyer AI and compare up to four apartments | Yes | Yes | Public view | Public view |
| Save favourites and submit an enquiry | Sign-in/verification required | Own account | Not a company-management operation | Not a buyer-enquiry operation |
| Read buyer enquiry history | No | Own records | Owning company inbox only | No separate buyer-history permission is defined |
| Edit private drafts, stock, media and mappings | No | No | Owned company only | Administration does not replace developer preparation |
| Publish a complete development | No | No | Owned company, if unrestricted | No routine prior approval step |
| Process and archive enquiries | No | No | Own inbox | No additional operational inbox role is defined |
| Create/suspend/reactivate company access | No | No | No | Yes |
| Hide/restore a development | No | No | Cannot remove an administrative restriction | Yes, with the required reason |
| Edit city/finishing references and inspect audit history | No | No | Uses permitted reference values | Yes |

## Ownership rules

The parent chain Company → Development → Building → Floor → Apartment determines content ownership. A region, file, finishing offer, parking place or enquiry inherits the appropriate object context. Substituting identifiers in a request cannot change the caller's scope.

A suspended developer cannot continue developer operations. Suspension preserves content and enquiries and removes company developments from public access. Reactivation follows the separate visibility rules in [[states]].

## Public visibility

Public reads use the same visibility decision across list results, map markers, AI results, direct links and file access. A saved comparison/favourite identifier does not bypass a development restriction. Reserved/Sold apartment detail remains readable only when its development remains public; the new-enquiry action is disabled.

## Account boundaries

Buyer email verification is required before account access. One developer account represents each manually verified company. Public company self-registration and staff-account delegation are excluded. See [[accounts]], [[administration]] and [[requirements]] for their acceptance rules.
