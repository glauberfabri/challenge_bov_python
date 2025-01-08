from fastapi import APIRouter, HTTPException
from app.repositories.production_repository import create_production, get_production_by_month
from app.services.farmer_service import calculate_price
from app.services.production_service import get_semester, is_bonus_applicable
from app.models.milk_production import MilkProduction

router = APIRouter()

@router.post("/productions/")
def register_production(production: MilkProduction):
    create_production(production)
    return {"message": "Production registered successfully"}

@router.get("/price/{farm_id}/{month}")
def get_price(farm_id: str, month: str):
    productions = list(get_production_by_month(farm_id, month))
    if not productions:
        raise HTTPException(status_code=404, detail="No production found")

    total_volume = sum(p['volume'] for p in productions)
    semester = get_semester(productions[0]['date'])
    is_bonus = is_bonus_applicable(total_volume)
    price = calculate_price(total_volume, productions[0]['distance'], is_bonus, semester)
    return {"price": price}