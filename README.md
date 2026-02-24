# argument-quality-nlp-toolkit

A unified pipeline for argumentation mining and quality assessment using classical NLP and supervised ML techniques, built around the Dagstuhl-15512-ArgQuality corpus.

## Modules

| Module | Description |
|--------|-------------|
| `data_processor/` | Downloads and processes the Dagstuhl-15512-ArgQuality corpus, stores as JSON, creates ML splits, and computes statistics |
| `argument_unit_classification/` | Classifies argumentative units using text features and ML models |
| `argument_quality_assessment/` | Assesses essay quality on the confirmation bias dimension using supervised ML |
