"""Idempotent simulated gateway seam; production adapters must never store card data."""
from decimal import Decimal
from app.services.pricing_service import cents

class SimulatedPaymentGateway:
    def __init__(self): self.results = {}
    async def charge(self, idempotency_key: str, amount: Decimal, stage: str):
        if idempotency_key not in self.results:
            self.results[idempotency_key] = {"status": "succeeded", "amount": cents(amount), "stage": stage, "reference": f"SIM-{idempotency_key}"}
        return self.results[idempotency_key]
