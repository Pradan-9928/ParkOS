from pydantic import BaseModel

class LayoutPublishRequest(BaseModel):
    lot_id: str
    version: int
    layout: list[list[dict]]
