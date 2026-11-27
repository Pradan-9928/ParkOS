from dataclasses import dataclass

@dataclass
class User:
    id: str
    name: str
    phone: str

@dataclass
class Vehicle:
    id: str
    user_id: str
    plate: str | None = None
