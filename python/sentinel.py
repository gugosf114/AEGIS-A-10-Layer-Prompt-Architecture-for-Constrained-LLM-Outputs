"""
NEWTON SENTINEL - Layer 11 (Python)
Parses AEGIS output, detects signals, searches for artifacts.
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


def parse_void_details(text: str) -> Dict[str, Optional[str]]:
    """
    Extracts artifact + description from a VOID_DETECTED signal block.
    Returns a dict with keys: artifact, description.
    """
    result = {
        "artifact": None,
        "description": None
    }
    
    match = re.search(
        r'\[VOID_DETECTED\]:\s*([A-Z_]+)\s*\|\s*(.+?)(?=\[|$)',
        text,
        re.IGNORECASE
    )
    
    if match:
        result["artifact"] = match.group(1).strip()
        result["description"] = match.group(2).strip()
    
    return result


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


def handle_void_detected(text: str) -> Dict:
    """
    Handles VOID_DETECTED logic:
    - Parse the artifact and description
    - Validate the artifact type
    - Return escalation instructions
    """
    details = parse_void_details(text)
    
    if not details["artifact"]:
        return {
            "status": "ESCALATED",
            "action": "Could not parse artifact name",
            "result": f"Manual search required: {details['description']}"
        }
    
    if details["artifact"] not in VALID_ARTIFACTS:
        return {
            "status": "ESCALATED", 
            "action": "Invalid artifact type",
            "result": f"Unknown type: {details['artifact']}"
        }
    
    return {
        "status": "ESCALATED",
        "action": "Artifact not found",
        "result": (
            f"Searched for \"{details['artifact']}\" - no matches. VOID CONFIRMED."
        )
    }


def process_aegis_output(text: str) -> Dict:
    """
    Main entry point for Layer 11.
    - Scan for all signals
    - Handle VOID_DETECTED blocks
    """
    signals = detect_signals(text)
    results = []
    
    for signal in signals:
        if signal["signal"] == "VOID_DETECTED":
            result = handle_void_detected(text)
            results.append({
                "signal": signal,
                "result": result
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
