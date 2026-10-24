# Buyer AI Selection

The buyer assistant converts natural-language preferences into supported catalogue conditions and explains matching apartments. The language model interprets the request; the backend owns validation, catalogue retrieval and commercial facts.

Requirements: FR-23–FR-26 and NFR-03/NFR-08. See [[requirements]].

## Interaction

The floating Find apartment button opens a compact overlay on catalogue and property pages. Expanded desktop mode places conversation and conditions beside result cards. Mobile mode occupies the screen. Opening an apartment minimises the assistant; reopening it retains the current conversation and conditions. Browser-restart persistence is not required.

Visitors can use the assistant without signing in. Favourite and enquiry actions from a result use the same verified-buyer gate as ordinary navigation.

## Selection sequence

1. The buyer describes preferences in Russian, Kazakh or English.
2. Local Qwen3 through Ollama extracts supported fields and identifies material ambiguity.
3. The application validates values and clarifies ambiguity that affects selection.
4. The backend retrieves public Available apartments satisfying explicit hard conditions, including city and budget.
5. Softer preferences affect ordering. Each explanation refers to known catalogue/infrastructure facts and the actual returned apartment.

An empty exact-match set is stated explicitly. The assistant proposes a specific condition change and searches with that change only after buyer confirmation. It cannot silently raise the budget or change the city to produce results.

The response language follows the buyer's message independently of the interface language. UI translations, stored public text and model interpretation are separate responsibilities.

## Data boundaries

Structured model output is checked against supported values. A syntactically valid JSON response is not sufficient evidence of correct interpretation. The model cannot invent apartment identifiers, prices, availability or missing infrastructure facts. A result opening preserves an explicitly selected valid finishing offer; otherwise the apartment base condition is used.

Developer-document retrieval/question answering, interior generation and rental-income estimates are outside this module. A rental-use preference can guide supported location/finishing comparisons without introducing an investment prediction service.

## Failure and acceptance

If interpretation fails or produces unsupported fields, the interface can request clarification while ordinary catalogue filtering remains available. Model resource fit and each supported language are checked on the selected artifact rather than inferred from general benchmarks.

The initial evaluation uses two equivalent request meanings in each language: a matching case and an empty-result case. Returned IDs, hard constraints, explanations and confirmed relaxation are compared with manual filtering. See [[verification]], [[contracts]] and [[apartments]].
