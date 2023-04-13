from fastapi import APIRouter

router = APIRouter (
    prefix="/clickUp",
    tags=['sync']
)


@router.post("/syncData")
async def syncData():
    return "holita"