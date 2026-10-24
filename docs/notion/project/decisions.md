# Design Decisions and Risks

This register summarises the current agreed design. Grouped references identify the original stakeholder decisions; later clarifications are reflected in the current wording. Requirement definitions and acceptance criteria are in [[requirements]].

<table fit-page-width="true" header-row="true">
	<tr>
		<td>Area</td>
		<td>Current decision</td>
		<td>Decision references</td>
	</tr>
	<tr>
		<td>Project identity</td>
		<td>QONYS retains the approved full project title. Temirlan Almukhamedov is Systems Analyst and Technical Coordinator, Yevgeniy Averyanov owns backend, Bexultan Nishanbek owns Flutter Web/frontend, and Islam Omirzak is supervisor.</td>
		<td>DEC-12, DEC-55</td>
	</tr>
	<tr>
		<td>Roles and catalogue</td>
		<td>Buyer, property developer and administrator; a shared city-based development catalogue with list and map views.</td>
		<td>Stakeholder functional basis</td>
	</tr>
	<tr>
		<td>Buyer access</td>
		<td>Email/password, mandatory verification before account access, email recovery. Guests browse, use AI and compare; favourites and enquiries require verified sign-in.</td>
		<td>DEC-09, DEC-22</td>
	</tr>
	<tr>
		<td>Buyer account</td>
		<td>Favourites, My enquiries and Account settings. Name, surname and phone are optional until an enquiry needs them; editable and prefilled/correctable in the enquiry. Password can change; email is displayed. Guest comparison survives sign-in.</td>
		<td>DEC-19, DEC-65</td>
	</tr>
	<tr>
		<td>Physical apartment</td>
		<td>Each apartment has a separate record, number, floor, plan, characteristics, price and physical availability. Layout lists show individual apartments.</td>
		<td>DEC-23, DEC-24</td>
	</tr>
	<tr>
		<td>Finishing</td>
		<td>The developer configures the base condition and price. Extra finishing variants and example photos are optional. A compact selector below the price shows full prices; one condition appears as text. Base preselection yields to a valid explicit comparison/AI context.</td>
		<td>DEC-58, DEC-62, DEC-63</td>
	</tr>
	<tr>
		<td>Price presentation and enquiries</td>
		<td>Catalogue cards can show the minimum offered price with From. The server rechecks the selected offer, price and availability; changed prices need confirmation and removed offers need reselection. Accepted enquiries retain their submitted snapshot.</td>
		<td>DEC-56, DEC-63</td>
	</tr>
	<tr>
		<td>Availability</td>
		<td>Available, Reserved and Sold belong to the physical apartment. Reserved/Sold are excluded from new selection but retained in saved comparison/favourites with current status; direct details remain readable when the development is public, with enquiries disabled.</td>
		<td>DEC-47</td>
	</tr>
	<tr>
		<td>Floor colours</td>
		<td>Available has no status fill; Reserved has translucent yellow and Sold translucent red. Unavailable regions are not selectable.</td>
		<td>Stakeholder functional basis</td>
	</tr>
	<tr>
		<td>Comparison</td>
		<td>Up to four individual apartments across developments/developers, retaining selected finishing, full price and identity.</td>
		<td>DEC-25, DEC-65</td>
	</tr>
	<tr>
		<td>Buyer AI</td>
		<td>Local Qwen3/Ollama extracts supported preferences. The backend validates hard constraints and searches actual public Available stock. Explanations use catalogue/infrastructure evidence; ambiguity prompts clarification. No exact match leads to a specific proposed change requiring buyer confirmation.</td>
		<td>DEC-26, DEC-27, DEC-53</td>
	</tr>
	<tr>
		<td>Assistant placement</td>
		<td>Floating launcher, compact overlay, expanded desktop view and mobile screen view. Opening an apartment minimises the assistant and retains current-session context.</td>
		<td>DEC-29</td>
	</tr>
	<tr>
		<td>Languages</td>
		<td>Russian, Kazakh and English UI and buyer AI. The assistant replies in the message language. Every populated public description/caption has three text versions; proper names, addresses and identifiers are exempt.</td>
		<td>DEC-28, DEC-30, DEC-32, DEC-57, DEC-61</td>
	</tr>
	<tr>
		<td>Developer account</td>
		<td>Administrator creation after manual company verification, one account per company, emailed password activation and email recovery.</td>
		<td>DEC-48</td>
	</tr>
	<tr>
		<td>Private preparation</td>
		<td>The developer saves and resumes gradual private drafts. Initial publication requires the complete mandatory minimum. Later valid saves are immediately public, subject to administrative restrictions.</td>
		<td>DEC-34, DEC-37, DEC-64</td>
	</tr>
	<tr>
		<td>Developer navigation</td>
		<td>Four global workspace sections and nine editing sections within a development. Descriptions use defined text fields and a gallery, with three language versions.</td>
		<td>DEC-32, DEC-35</td>
	</tr>
	<tr>
		<td>Repeated floors and bulk edits</td>
		<td>Reviewed geometry can be copied to matching floors while target apartment identities and commercial state remain separate. The apartment list supports bulk price and availability edits.</td>
		<td>DEC-33, DEC-36</td>
	</tr>
	<tr>
		<td>Region assistance</td>
		<td>SAM 2/OpenCV with project-specific processing supplies candidate geometry. Developers correct or draw regions and explicitly assign owned floor/apartment records before saving reviewed mappings.</td>
		<td>DEC-54</td>
	</tr>
	<tr>
		<td>Enquiries</td>
		<td>Apartment/parking context is attached automatically. Enquiries reach the owning inbox and SMTP notification queue. Statuses are New, In progress, Processed and Cancelled; completed records can be archived, without developer permanent deletion. Public manager numbers are absent.</td>
		<td>DEC-18, DEC-20, DEC-21</td>
	</tr>
	<tr>
		<td>Visibility controls</td>
		<td>Administrators suspend/reactivate developer access and hide/restore developments. The developer sees the hiding reason. Reactivation preserves individual restrictions and private drafts.</td>
		<td>DEC-14, DEC-17, DEC-49</td>
	</tr>
	<tr>
		<td>Reference data and audit</td>
		<td>Editable city and finishing lists protect referenced values from deletion; deactivation preserves existing use/search. Audit covers key access, visibility, price and availability changes. Overview shows developer, buyer, published and hidden-development counts. Buyer blocking is excluded.</td>
		<td>DEC-50, DEC-51, DEC-52</td>
	</tr>
	<tr>
		<td>Architecture and storage</td>
		<td>Flutter Web, modular Django/DRF, shared PostgreSQL, Celery/RabbitMQ and server filesystem storage through Django with ownership/metadata in PostgreSQL.</td>
		<td>DEC-40, DEC-41</td>
	</tr>
	<tr>
		<td>Maps and infrastructure</td>
		<td>OSM/flutter_map; infrastructure is retained in the database and can be corrected or supplemented by the developer.</td>
		<td>DEC-42</td>
	</tr>
	<tr>
		<td>Optional assets</td>
		<td>Supplied GLB site/apartment scenes use Three.js. Supplied panoramic JPEG tours use Pannellum. Each public action appears only when its content exists.</td>
		<td>DEC-43</td>
	</tr>
	<tr>
		<td>Evaluation and priorities</td>
		<td>Lightweight single-user workflow and AI checks. Requirement priorities are an implementation draft for later detailed scheduling.</td>
		<td>DEC-59, DEC-60</td>
	</tr>
	<tr>
		<td>Exclusions</td>
		<td>Developer chatbot, interior generation, developer-document question answering, automatic 3D reconstruction, payments, automatic reservations and a native mobile application.</td>
		<td>Explicit stakeholder exclusions</td>
	</tr>
</table>

## Technical and delivery risks


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


## Documentation conventions

The overview-count definitions in [[administration]] are a documentation-level design convention for a consistent implementation and controlled-fixture check. They define the four approved counters without introducing new user-management functionality. Logical operation names in [[contracts]] define design interactions rather than implemented routes. The processing vocabulary in [[jobs]] describes work progress independently of business states.

The six additional interview requests remain in [[defence]] as extension proposals: spreadsheet import, price-update dates, guest saving, written responses, price per square metre and rental-market comparisons. They do not silently expand the current requirement baseline.
