# AEGIS: A 10-Layer Prompt Architecture for Constrained LLM Outputs

AEGIS (Adversarial Evidence Governance & Integrity System) is a prompt architecture that reduces LLM drift by systematically constraining the model's output space. Instead of asking AI to "summarize" or "analyze," AEGIS forces evidence classification, conflict detection, and audit-grade outputs.

## The Problem

Most people use AI like a search box. Upload documents, ask questions, hope the answers are accurate.

The problem is **drift**. Over time, the model:
- Blends sources instead of separating them
- Hedges conclusions with vague language
- Smooths contradictions instead of flagging them

You asked for an audit. You got a summary.

## The Solution

AEGIS is a 10-layer prompt structure that constrains the model's degrees of freedom until it produces auditable, evidence-classified outputs.

| Layer | Name | Function |
|-------|------|----------|
| 1 | System Prompt | Role lock, clinical tone, NO list |
| 2 | Kernel | 3-Pass Compilation (Ingest → Collide → Synthesize) |
| 3 | Governor | Schism detection, severity triage, linter |
| 4 | Controller | Circuit breaker, override, pagination |
| 5 | Sentinel | Genealogy tracking, CYA detection |
| 6 | Omega | Session ledger, operator drift, self-doubt |
| 7 | Aegis | Void detection, sterility warning, falsification |
| 8 | Rosetta | Semantic normalization, definition matching |
| 9 | Oracle | Counterfactual simulation, risk prediction |
| 10 | Chameleon | Dynamic domain adaptation |

## Quick Start

Copy the contents of [`bootloader.txt`](bootloader.txt) into any LLM's system prompt or first message. Works with GPT-4, Claude, Gemini, Llama, or any model that accepts system instructions.

## What It Does

- **Truth Hierarchy**: Enforces Class A (Logs, Timestamps) > Class B (Emails, Memos) > Class C (Roadmaps, Drafts)
- **Schism Detection**: Flags conflicts between sources with severity ratings (FATAL, HIGH, WARN)
- **Void Detection**: Identifies missing artifacts instead of assuming they exist
- **Adversarial Detection**: Surfaces patterns indicating after-the-fact documentation
- **Falsification Keys**: Demands "To prove this wrong, produce X"

## Validation

In testing, AEGIS surfaced 5 unsupported claims and 5 missing artifacts that a standard prompt missed entirely.

## Files

- `bootloader.txt` — The complete 10-layer prompt (copy/paste ready)
- `Newton_Sentinel.gs` — Google Apps Script for automated signal processing (Layer 11)
- `examples/` — Test cases and sample outputs
- `AEGIS_10Layer_Architecture.pdf` — Full paper with methodology

## Limitations

AEGIS improves audit-style outputs but cannot:
- Verify forged Class A artifacts
- Resolve genuinely ambiguous evidence without operator input
- Guarantee identical outputs across runs (LLMs remain probabilistic)

## License

MIT — Use it, fork it, improve it.

## Author

George Abrahamyants  
December 2025

---

*"Drift happens when the model has choices. Remove the choices, reduce the drift."*

