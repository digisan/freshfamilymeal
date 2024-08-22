from fastapi import APIRouter
from pydantic import BaseModel, StrictInt


class Menu(BaseModel):
    id: StrictInt
    Name: str
    Description: str
    Ingredients: str
    NutritionalInfo: str
    Allergens: str
    Instructions: str
    Image: bytes


# create router
router = APIRouter(prefix="/menu", tags=["Menu"])


@router.get("/list")
async def list_dishes():
    return {"message": "all available dishes."}


@router.post("/add-dish")
async def add_dish():
    return {"message": "we are adding a new dish."}


@router.delete("/remove-dish")
async def remove_dish():
    return {"message": "we are removing a dish."}
