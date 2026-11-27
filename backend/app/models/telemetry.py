from dataclasses import dataclass
from datetime import datetime

@dataclass
class TelemetryEvent:
    id: str
    lot_id: str
    slot_id: str | None
    source: str
    created_at: datetime
