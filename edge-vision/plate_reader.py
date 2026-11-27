"""ANPR integration boundary. Supply a vendor detector in the deployed edge image."""
from dataclasses import dataclass
import re

@dataclass
class PlateReading:
    plate: str
    confidence: float
    gate: str
    captured_at: float

def normalize_plate(value: str) -> str:
    return re.sub(r"[^A-Z0-9-]", "", (value or "").upper())

class PlateReader:
    def __init__(self, detector=None, threshold: float = 0.85):
        self.detector = detector
        self.threshold = threshold

    def read(self, frame, gate: str, captured_at: float) -> PlateReading | None:
        if self.detector is None:
            return None
        result = self.detector(frame)
        if not result:
            return None
        plate = normalize_plate(result.get("plate", ""))
        confidence = float(result.get("confidence", 0.0))
        if len(plate) < 2 or len(plate) > 12 or confidence < self.threshold:
            return None
        return PlateReading(plate=plate, confidence=confidence, gate=gate, captured_at=captured_at)
