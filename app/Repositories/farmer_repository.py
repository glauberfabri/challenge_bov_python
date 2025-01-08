from app.config import db

def create_farmer(farmer):
    db.farmers.insert_one(farmer.dict())

def get_farmer_by_id(farmer_id):
    return db.farmers.find_one({"id": farmer_id})