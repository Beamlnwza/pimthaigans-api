from fastapi import APIRouter

router = APIRouter(
    prefix="/view",
    tags=["View"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def info():
    return {"info": "This is the generate endpoint"}


@router.get("/status")
async def status():
    return {"status": "OK"}
