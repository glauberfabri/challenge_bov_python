from fastapi import FastAPI
from app.controllers.farmer_controller import router as farmer_router
from app.controllers.production_controller import router as production_router

app = FastAPI()

app.include_router(farmer_router, prefix="/api")
app.include_router(production_router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Milk Management API"}