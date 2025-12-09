# 🛡️ AEGIS — 10-Layer Prompt Architecture for Constrained LLM Outputs  
### + Newton Sentinel (Layer 11, Python Runtime Engine)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![Apps Script](https://img.shields.io/badge/Apps%20Script-Google-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Status: Active](https://img.shields.io/badge/Status-Active-brightgreen.svg)
![Deterministic AI](https://img.shields.io/badge/Deterministic-AI-blueviolet.svg)
![Forensic Control](https://img.shields.io/badge/Forensic-Control-critical.svg)
![AEGIS Framework](https://img.shields.io/badge/AEGIS-10--Layer%20Architecture-navy.svg)
![Newton Sentinel](https://img.shields.io/badge/Newton-Sentinel-important.svg)

---

## 📘 Overview

**AEGIS** is a 10-layer forensic prompt architecture designed to control, constrain, and audit LLM outputs.  
It enforces:

- truth hierarchies  
- conflict detection  
- void detection  
- escalation logic  
- deterministic reasoning  
- operator-controlled responses  

**Newton Sentinel (Layer 11)** is the Python runtime engine that interprets AEGIS signals, processes VOID blocks, validates artifacts, and outputs machine-verifiable escalation objects.

Together, they form a **deterministic AI governance and analysis stack** suitable for:

- compliance  
- audit defense  
- risk analysis  
- enterprise governance  
- structured AI workflows  
- regulated environments  

---

# 🧩 AEGIS — 10-Layer Architecture (Summary)

AEGIS organizes LLM reasoning into layers:

| Layer | Function |
|-------|----------|
| **1 – 3** | Truth hierarchy, evidence classes, immutable vs mutable sources |
| **4 – 6** | Schism Engine, conflict detection, logic triage |
| **7 – 9** | Forensic structuring, void detection, anomaly reporting |
| **10** | Operator Command Layer (explicit directives, overrides) |
| **11** | **Newton Sentinel (Python runtime)** |

AEGIS is implemented in Apps Script and/or Python for:

- deterministic execution  
- logging  
- auditability  
- forensic replay  

---

# ⚙️ How AEGIS Interacts with Newton Sentinel

```
[User Input]  
   ↓  
[AEGIS Bootloader (Layers 1–10)]  
   ↓ (structured forensic output)  
[Newton Sentinel – Layer 11 (Python)]  
   ↓  
[Deterministic Escalation / Interpretation]  
   ↓  
[Operator / System Log / Compliance Layer]
```

Sentinel is the **execution engine** that interprets AEGIS’s structured signals.

---

# 🐍 Newton Sentinel — Layer 11 (Python Runtime Engine)

`python/sentinel.py` performs:

- multi-block VOID_DETECTED parsing  
- signal detection  
- artifact validation  
- forensic escalation logic  
- deterministic output generation  
- AEGIS → Python integration  

It ensures that LLM outputs become **structured, auditable, machine-verifiable events**.

---

## 🔥 Core Features

- **Multi-block VOID_DETECTED parser**  
  Extracts *every* VOID block, not just the first.

- **Artifact whitelist validation**  
  Ensures artifacts map to valid document types.

- **Complete signal extraction**  
  Handles `[VOID_DETECTED]`, `[FATAL]`, `[HIGH]`, `[SYSTEM_HALT]`, `[ADVERSARIAL_SUSPICION]`, etc.

- **Deterministic escalation objects**  
  Produces machine-stable, audit-ready outputs.

- **Designed for replay**  
  Same input → same output → stable forensic behavior.

---

# 📄 VOID Block Format (Supported)

```
[VOID_DETECTED]: ARTIFACT_NAME | Description text here…
```

Examples:

```
[VOID_DETECTED]: INCIDENT_TICKET | No incident record found for March 15 purge
[VOID_DETECTED]: BACKUP_LOG | Snapshot missing prior to restore operation
```

AEGIS may emit **multiple** VOID blocks; Sentinel parses all of them.

---

# 🚀 Example: Using Sentinel to Process AEGIS Output

### **Python Code Example**

```python
from sentinel import process_aegis_output

text = """
[VOID_DETECTED]: INCIDENT_TICKET | Incident record for March 15 purge
[VOID_DETECTED]: BACKUP_LOG | Post-incident snapshot confirming restore
"""

result = process_aegis_output(text)
print(result)
```

---

# 🧩 Example Output (Deterministic JSON)

```json
{
  "signals_found": 2,
  "results": [
    {
      "signal": "VOID_DETECTED",
      "result": {
        "status": "ESCALATED",
        "action": "Artifact not found",
        "result": "Searched for \"INCIDENT_TICKET\" - no matches. VOID CONFIRMED."
      }
    },
    {
      "signal": "VOID_DETECTED",
      "result": {
        "status": "ESCALATED",
        "action": "Artifact not found",
        "result": "Searched for \"BACKUP_LOG\" - no matches. VOID CONFIRMED."
      }
    }
  ]
}
```

---

# 📂 Project Structure

```
/
├── python/
│   └── sentinel.py          # Newton Sentinel (Layer 11)
├── apps_script/
│   └── aegis_bootloader.gs  # AEGIS Layers 1–10 (optional)
├── docs/
│   └── architecture.md
│   └── examples.md
├── README.md
└── LICENSE
```

---

# 🧪 Testing (Optional)

To validate Sentinel:

```
python3 python/sentinel.py
```

---

# 📜 License

This project is licensed under the **MIT License**, allowing open use, modification, and distribution.

---

# 🤝 Contributing

Contributions are welcome, especially around:

- new forensic signals  
- additional artifact types  
- improved regex parsing  
- CLI wrappers  
- AEGIS–Sentinel integration  

Submit a PR or open an issue.

---

# ⭐ Final Notes

This repository demonstrates an advanced **deterministic AI control framework**, pairing structured LLM prompting (AEGIS) with formal forensic interpretation (Newton Sentinel).  
It is designed for reliability, auditability, and operational clarity in complex workflows.

---

