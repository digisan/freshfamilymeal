from fastapi import APIRouter
from pydantic import BaseModel, StrictInt
from datetime import datetime


class Cooking(BaseModel):
    id: StrictInt
    MealId: StrictInt
    ServingNum: StrictInt
    ServingUnit: str
    ScheduledTime: datetime
    CookedBy: str
    MadeTm: datetime
    KitchenAddr: str
    Image: bytes
    Video: bytes
    FinalProcId: StrictInt


# create router
router = APIRouter(prefix="/cooking", tags=["Cooking"])


@router.post("/schedule")
async def schedule():
    return {"message": "we are scheduling a cooking."}


@router.post("/process")
async def process():
    return {"message": "we are cooking now."}
