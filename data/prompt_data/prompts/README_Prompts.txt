# Or HaSugya Schema-Driven Prompt Suite

## Exact filenames

Shared files:

- `OrHaSugya_OutputSchema.json`
- `OrHaSugya_AnalysisStandards.json`

Prompt files:

- `sugyaAnalysisPrompt.txt`
- `sugyaAuthorityAnalysisPrompt.txt`
- `sugyaArgumentAnalysisPrompt.txt`
- `sugyaSourceRelationshipAnalysisPrompt.txt`
- `sugyaExegesisAnalysisPrompt.txt`

Pipeline data files:

- `<TRACTATE>_bundle.jsonl`
- `<TRACTATE>_sugya_analysis.json`
- `<TRACTATE>_authority_analysis.json`
- `<TRACTATE>_argument_analysis.json`
- `<TRACTATE>_source_relationship_analysis.json`
- `<TRACTATE>_exegesis_analysis.json`

Replace `<TRACTATE>` with the tractate name used by the project.

Do not add version numbers or suffixes to filenames. Version history is managed through Git.

## Pipeline order

1. `sugyaAnalysisPrompt.txt`
   - Input: `<TRACTATE>_bundle.jsonl`
   - Output: `<TRACTATE>_sugya_analysis.json`

2. `sugyaAuthorityAnalysisPrompt.txt`
   - Inputs: `<TRACTATE>_sugya_analysis.json`, `<TRACTATE>_bundle.jsonl`
   - Output: `<TRACTATE>_authority_analysis.json`

3. `sugyaArgumentAnalysisPrompt.txt`
   - Inputs: `<TRACTATE>_sugya_analysis.json`, `<TRACTATE>_bundle.jsonl`,
     `<TRACTATE>_authority_analysis.json`
   - Output: `<TRACTATE>_argument_analysis.json`

4. `sugyaSourceRelationshipAnalysisPrompt.txt`
   - Inputs: `<TRACTATE>_bundle.jsonl`, `<TRACTATE>_sugya_analysis.json`,
     `<TRACTATE>_authority_analysis.json`, `<TRACTATE>_argument_analysis.json`
   - Output: `<TRACTATE>_source_relationship_analysis.json`

5. `sugyaExegesisAnalysisPrompt.txt`
   - Inputs: `<TRACTATE>_bundle.jsonl`, `<TRACTATE>_sugya_analysis.json`,
     `<TRACTATE>_authority_analysis.json`, `<TRACTATE>_argument_analysis.json`,
     `<TRACTATE>_source_relationship_analysis.json`
   - Output: `<TRACTATE>_exegesis_analysis.json`

## Schema behavior

`OrHaSugya_OutputSchema.json` now defines:

- the exact prompt filename for every stage;
- all required input filenames;
- the exact output filename;
- the complete output field structure;
- conditional-field and empty-value rules.

Every prompt repeats its own exact file contract so the filename requirements remain
visible even when the prompt is read separately.
