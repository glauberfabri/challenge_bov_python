from pydantic import BaseModel

class Farmer(BaseModel):
    id: str
    name: str
    farm_name: str
    distance_to_factory: float  # Em KM
