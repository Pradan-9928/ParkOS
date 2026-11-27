from decimal import Decimal, ROUND_HALF_UP

def cents(value) -> Decimal:
    return Decimal(str(value)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

def estimate(hourly_rate, hours, multiplier=1):
    return cents(Decimal(str(hourly_rate)) * Decimal(str(hours)) * Decimal(str(multiplier)))

def overstay_fee(hourly_rate, overdue_hours, multiplier=Decimal("1.5")):
    return cents(Decimal(str(hourly_rate)) * Decimal(str(overdue_hours)) * Decimal(str(multiplier)))
