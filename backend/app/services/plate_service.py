"""Normalize and validate plate readings before matching active sessions."""
import re

def normalize_plate(value: str) -> str:
    return re.sub(r"[^A-Z0-9-]", "", (value or "").upper())

def accept_reading(value: str, confidence: float, threshold: float = 0.85) -> dict:
    plate = normalize_plate(value)
    confidence = max(0.0, min(1.0, float(confidence)))
    if len(plate) < 2 or len(plate) > 12:
        return {"accepted": False, "reason": "invalid_plate", "plate": plate, "confidence": confidence}
    if confidence < threshold:
        return {"accepted": False, "reason": "low_confidence", "plate": plate, "confidence": confidence}
    return {"accepted": True, "plate": plate, "confidence": confidence}
