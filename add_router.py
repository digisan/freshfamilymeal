from fastapi import APIRouter

# create router
router = APIRouter(prefix="/add", tags=["addition"])


@router.get("/numbers")
def add_numbers():
    return {"message": "we are adding numbers. (1,2,3)"}


@router.get("/strings")
def add_strings():
    return {"message": "we are adding strings. ('abc')"}
