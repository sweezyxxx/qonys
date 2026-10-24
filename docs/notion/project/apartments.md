# Apartments Finishing and Comparison

This module maintains the identity, characteristics and commercial presentation of each physical apartment. Finishing changes the offered condition and price, while availability remains a property of the apartment.

Requirements: FR-09–FR-14, FR-22 and the commercial checks in FR-33. See [[requirements]].

## Physical apartment

Each apartment has a number, building/floor, room count, area, bathroom count, supplied 2D layout, developer-configured base condition, base price and availability. The base condition can be No finish, WhiteBox, finished delivery or another supported reference value. It is never inferred from absent photographs.

The apartment is valid without separately created extra finishing records or example photos. Extra offers may have their own full apartment price, description, images and optional apartment 3D model. They share the physical apartment's Available/Reserved/Sold state.

## Price and finishing selection

A compact selector appears below the price and before the main actions. Labels show the condition and full apartment price. A single condition appears as ordinary text. The base condition is initially selected unless a valid explicit comparison/AI context identifies another offer.

Selecting an offer updates its price, description and supplied media. It does not create another apartment or reset availability. Comparison and enquiries retain the selected offer. Catalogue cards may use the minimum offered price with a From label; that does not force the cheapest offer as the detail-page default.

## Comparison and favourites

Comparison accepts up to four apartments across developments and developers. Each column retains development, developer, location, rooms, area, floor, bathrooms, selected finishing, corresponding full price and availability. A fifth apartment is not added. Guest comparison survives sign-in.

Favourites require verified sign-in. Previously saved unavailable apartments remain with their status; content restricted at development level is protected. Guest favourites and rental-return prediction are outside the current baseline.

## Maintenance

The developer edits owned apartments and may apply bulk price/availability changes to a selected set. Other apartments and other companies remain unchanged. Copying a plan to another floor creates/reuses geometry references while preserving separate physical apartment identities and commercial records. Spreadsheet import is a separately recorded extension request, not part of bulk editing.

## Enquiry handover

The backend rechecks the apartment, offer, price, visibility and availability at submission. A changed price requires confirmation; a removed offer requires a valid replacement. The accepted enquiry keeps the submitted snapshot even after later price changes. See [[enquiries]] and [[contracts]].

Acceptance includes a usable base-only apartment, shared availability across offers, a four-item comparison limit, context-preserving sign-in and correct changed-price handling.
