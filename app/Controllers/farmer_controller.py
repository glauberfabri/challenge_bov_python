from fastapi import APIRouter, HTTPException
from app.repositories.farmer_repository import create_farmer, get_farmer_by_id
from app.models.farmer import Farmer

router = APIRouter()

@router.post("/farmers/")
def register_farmer(farmer: Farmer):
    if get_farmer_by_id(farmer.id):
        raise HTTPException(status_code=400, detail="Farmer already exists")
    create_farmer(farmer)
    return {"message": "Farmer registered successfully"}