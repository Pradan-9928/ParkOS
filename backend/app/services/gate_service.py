from datetime import datetime, timezone
from app.services.fsm_service import transition, BOOKING_TRANSITIONS

def check_in(booking):
    booking['status'] = transition(BOOKING_TRANSITIONS, booking['status'], 'CHECKED_IN')
    booking['entry_at'] = datetime.now(timezone.utc)
    return booking
