# QONYS working project documentation

[Open QONYS](https://app.notion.com/p/402878b53f0980a9bebafc8ef6d32613). The working specification is organised into seven sections and 22 topic pages.

## Working sections

- [01 Product](https://app.notion.com/p/403878b53f09812aba09fce6a416c47e).
- [02 Functional Modules](https://app.notion.com/p/403878b53f0981ca9a18c9880a0883e7).
- [03 Architecture and Data](https://app.notion.com/p/403878b53f0981e69a91f93faf714427).
- [04 Interfaces and Processing](https://app.notion.com/p/403878b53f0981dfb262eaf09615cd6e).
- [05 UX and Content](https://app.notion.com/p/403878b53f098130959ed38e680c26e9).
- [06 Quality and Verification](https://app.notion.com/p/403878b53f09819f9d93e8140259ee00).
- [07 Team and Delivery](https://app.notion.com/p/403878b53f0981a6b947f0cdba11cbb2).

The nine functional modules cover accounts, catalogue/spatial navigation, apartments/finishing/comparison, content/publication, buyer AI, image regions, enquiries, administration, and maps/parking/visual assets. Architecture, data dictionaries, states, logical contracts, background/file processing, UX/content, acceptance and delivery rules have their own pages.

## Defence snapshot

The previous submission pages are retained under [defence24.10.26](https://app.notion.com/p/403878b53f09815793b1d6ba8d168cbf). All fifteen top pages, three interview pages, Word/Markdown/archive attachments and prototype assets preserve their existing IDs and links. The snapshot is separate from the living project specification.

## Local sources

- project/*.md contains the working English page sources. Double-bracket references identify page slugs resolved during publication.
- project/pages.json records the current page IDs, hierarchy and functional ownership.
- project/publishing-state.json records verification of the published structure and contents.
- scripts/build_project_documentation.py builds the native Notion payloads locally without publishing them.

The current matrix contains 40 functional and 10 non-functional requirements. All functional requirements have module ownership. Publication verification read back all 29 working pages, compared their text, checked native child-page relationships and internal references, and confirmed the retained defence assets. Earlier migration records describe previous publications and are retained as history.
