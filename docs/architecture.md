# Architecture - AI Data Quality Assistant on Databricks

## High-Level Architecture

```text
Data Quality Reports (CSV)
        |
        v
Bronze Delta Tables
Raw validation, summary, and history reports
        |
        v
Gold Quality Metrics
Aggregated table-level and rule-level quality metrics
        |
        v
RAG Documents
Natural-language documents generated from structured quality metrics
        |
        v
Agent Tools
Python/PySpark tools for quality investigation
        |
        v
AI Assistant
Business-friendly data quality explanation and remediation plan
```

---

## Data Layer

### Bronze Layer

Stores raw validation outputs.

Tables:

- bronze_validation_report
- bronze_summary_report
- bronze_quality_history

Purpose:

- Preserve source reports
- Enable traceability
- Support auditing

---

## Gold Layer

Stores aggregated quality metrics.

Tables:

- gold_quality_by_table
- gold_quality_by_rule

Provides:

- Quality score analysis
- Failed rule analysis
- Table-level monitoring

---

## RAG Layer

Transforms structured metrics into natural-language documents.

Example:

```text
Table customers has quality score 82.86 with 7 failed rules.
```

Purpose:

- LLM-friendly context
- Future vector search integration
- Semantic retrieval

---

## Agent Layer

### Tool 1

`get_worst_quality_table()`

Returns the table with the lowest quality score.

### Tool 2

`get_failed_rules(table_name)`

Returns failed rules and failure percentages.

### Tool 3

`generate_remediation_plan(table_name)`

Returns recommended remediation actions.

---

## Agent Flow

```text
User Question
      |
      v
Agent
      |
      v
Tool Selection
      |
      v
Delta Tables
      |
      v
Evidence Collection
      |
      v
Business Response
```

---

## Current Status

| Component | Status |
|-----------|---------|
| GitHub Integration | ✅ |
| Databricks Setup | ✅ |
| Bronze Layer | ✅ |
| Gold Layer | ✅ |
| RAG Documents | ✅ |
| Agent Tools | ✅ |
| Response Generator | ✅ |
| Vector Search | Planned |
| Foundation Models | Planned |
| Agent Serving | Planned |

---

## Future Target Architecture

```text
User Question
      |
      v
Databricks Agent
      |
      +-------------------------+
      |                         |
      v                         v
Delta Query Tool       Vector Search Retriever
      |                         |
      v                         v
Gold Metrics           RAG Documents
      |                         |
      +------------+------------+
                   |
                   v
                LLM
                   |
                   v
         Final Recommendation
```