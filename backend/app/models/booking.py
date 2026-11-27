from dataclasses import dataclass
from datetime import datetime

@dataclass
class Booking:
    id: str
    user_id: str
    slot_id: str
    status: str
    expires_at: datetime

@dataclass
class TimeExtension:
    booking_id: str
    added_minutes: int
    amount: str
