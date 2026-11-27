from pydantic import BaseModel, Field

class BookingRequest(BaseModel):
    lot_id: str
    slot_id: str = Field(min_length=1, max_length=32)
    name: str = Field(min_length=1, max_length=80)
    phone: str = Field(min_length=7, max_length=20)
    plate: str | None = Field(default=None, max_length=12)
    hours: float = Field(gt=0, le=72)
