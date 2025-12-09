"""
NEWTON SENTINEL - Layer 11 (Python)
Parses AEGIS output, detects signals, extracts VOID blocks,
validates artifacts, and produces deterministic forensic escalations.
"""

import re
from typing import Optional, Dict, List


# Valid artifact types
VALID_ARTIFACTS = [
    "BACKUP_LOG",
    "INCIDENT_TICKET",
    "CHANGE_RECORD",
    "APPROVAL_DOC",
    "AUDIT_TRAIL",
    "TIMESTAMP_LOG",
    "ESCALATION_RECORD"
]

# Signals this layer responds to
SIGNAL_TAGS = [
    "[VOID_DETECTED]",
    "[SCHISM_CRITICAL]",
    "[ADVERSARIAL_SUSPICION]",
    "[SYSTEM_HALT]",
    "[FATAL]",
    "[HIGH]"
]


def parse_void_details(text: str) -> List[Dict[str, Optional[str]]]:
    """
    Extracts ALL VOID_DETECTED blocks from the input text.
    Multi-block aware.

    Returns:
      [
        {"artifact": str or None, "description": str or None},
        ...
      ]
    """
    matches = re.findall(
        r'\[VOID_DETECTED\]:\s*([A-Z_]+)\s*\|\s*(.+?)(?=\[|$)',
        text,
        re.IGNORECASE | re.DOTALL
    )

    results = []
    for artifact, desc in matches:
        results.append({
            "artifact": artifact.strip(),
            "description": desc.strip()
        })

    if not results:
        results.append({"artifact": None, "description": None})

    return results


def detect_signals(text: str) -> List[Dict]:
    """
    Detects all known signal tags in the text.
    Returns a list of signal objects.
    """
    detected = []

    for tag in SIGNAL_TAGS:
        if tag in text:
            detected.append({
                "tag": tag,
                "signal": tag.strip("[]")
            })

    return detected


def handle_void_detected(text: str) -> List[Dict]:
    """
    Handles VOID_DETECTED logic for ALL detected blocks.
    Returns a list of escalation objects.
    """
    parsed_blocks = parse_void_details(text)
    escalations = []

    for block in parsed_blocks:
        artifact = block["artifact"]
        desc = block["description"]

        if not artifact:
            escalations.append({
                "status": "ESCALATED",
                "action": "Could not parse artifact name",
                "result": f"Manual search required: {desc}"
            })
            continue

        if artifact not in VALID_ARTIFACTS:
            escalations.append({
                "status": "ESCALATED",
                "action": "Invalid artifact type",
                "result": f"Unknown type: {artifact}"
            })
            continue

        escalations.append({
            "status": "ESCALATED",
            "action": "Artifact not found",
            "result": f"Searched for \"{artifact}\" - no matches. VOID CONFIRMED."
        })

    return escalations


def process_aegis_output(text: str) -> Dict:
    """
    Main entry point for Layer 11.
    - Scan for all signals
    - Handle all VOID_DETECTED blocks
    - Support multi-block forensic output
    """
    signals = detect_signals(text)
    results = []

    for signal in signals:
        if signal["signal"] == "VOID_DETECTED":
            escalations = handle_void_detected(text)
            for e in escalations:
                results.append({
                    "signal": signal,
                    "result": e
                })

    return {
        "signals_found": len(signals),
        "results": results
    }


if __name__ == "__main__":
    test_input = """
    [VOID_DETECTED]: INCIDENT_TICKET | Incident record for March 15 purge
    [VOID_DETECTED]: BACKUP_LOG | Post-incident snapshot confirming restore
    """

    output = process_aegis_output(test_input)
    print(f"Signals found: {output['signals_found']}")
    for r in output["results"]:
        print(f"  {r['result']['action']}: {r['result']['result']}")
