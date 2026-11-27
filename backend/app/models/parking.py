from dataclasses import dataclass
from decimal import Decimal

@dataclass
class ParkingSlot:
    id: str
    lot_id: str
    zone: str
    tier: str
    hourly_rate: Decimal
    status: str = "AVAILABLE"
