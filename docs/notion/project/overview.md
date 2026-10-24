# Product Overview and Scope

QONYS helps buyers find and compare specific apartments from different property developers. A buyer can connect a listing to its development, building, floor plan, physical apartment, finishing condition and surrounding infrastructure. Developers prepare and maintain that information through an owned workspace. Administrators control developer access and development visibility.

## Project identity

Development of an AI-Powered Residential Real Estate Visualization and Intelligent Property Selection Platform with 3D Site Visualization, Floor-Level Layouts, and Interactive Mapping

This title is fixed. The application deliverable is Flutter Web with a Django API; a native mobile application is outside scope.

## Main journeys

| Actor | Journey | Outcome |
| --- | --- | --- |
| Buyer or visitor | City catalogue → development → building and floor → apartment → finishing → comparison or enquiry | An identifiable apartment and offer, with current availability and price context. |
| Property developer | Private draft → gradual content entry → region review and linking → completeness check → publication | A complete public development whose valid later saves appear immediately. |
| Administrator | Verify representative → create company access → manage restrictions and reference data | Controlled developer access and public content, with reasons and audit history. |

The Layouts list and buyer assistant provide alternative routes to an apartment. A new enquiry is a contact request; it does not reserve or purchase the property.

## Included capabilities

- Shared development discovery by city in list and map modes.
- Individual apartment records, building/floor navigation, availability, finishing offers, favourites and comparison of up to four apartments.
- Russian, Kazakh and English UI, buyer selection and populated public descriptions.
- Catalogue-grounded interpretation of buyer preferences using local Qwen3/Ollama.
- Correctable floor/apartment region suggestions using SAM 2/OpenCV with project-specific processing.
- Private developer preparation, complete initial publication, immediate valid updates, enquiries and SMTP notifications.
- Administrative restrictions, restoration, reference data, summary counts and key-change audit history.
- Optional supplied GLB scenes and panoramic JPEG tours; parking when offered.

## Exclusions

The developer chatbot, interior-design generation, developer-document question answering, automatic 3D reconstruction, payments, mortgage processing, automatic reservations, realtor roles, buyer blocking and separate company employee accounts are excluded.

## Documentation ownership

[[modules]] owns functional behaviour. [[data]] and [[states]] own entity meaning and integrity. [[contracts]] owns interactions between the client, API and workers. [[requirements]] provides the acceptance baseline. [[decisions]] records current choices and risks.

[[defence]] contains the separate 24 October submission, research sources, interview transcripts and milestone artifacts. Project rules are maintained in the working documentation rather than inferred from a report's chapter order.
