from dataclasses import dataclass
from decimal import Decimal

@dataclass
class PaymentTransaction:
    id: str
    booking_id: str
    stage: str
    amount: Decimal
    idempotency_key: str
    status: str
