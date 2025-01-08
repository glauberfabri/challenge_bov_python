from pydantic import BaseModel

class MilkProduction(BaseModel):
    id: str
    farm_id: str
    date: str  # YYYY-MM-DD
    volume: float  # Em litros
