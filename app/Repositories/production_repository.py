from app.config import db

def create_production(production):
    db.milk_productions.insert_one(production.dict())

def get_production_by_month(farm_id, month):
    return db.milk_productions.find({"farm_id": farm_id, "date": {"$regex": f"^{month}"}})