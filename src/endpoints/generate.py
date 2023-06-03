from fastapi import APIRouter
from src.libs.model import CganCols
from src.models.main import User, Method
from src.models.generate import GenerateResult, ImageResult

router = APIRouter(
    prefix="/generate",
    tags=["Generate"],
    responses={404: {"description": "Not found"}},
)

model = CganCols()


@router.get("/")
async def info():
    return {"info": "This is the generate endpoint"}


@router.get("/status")
async def status():
    return {"status": "OK"}


@router.post("/")
async def generate(user: User, index: int | None = None) -> GenerateResult:
    if index:
        result: GenerateResult = await generate_index(user, index)
        return result

    return await generate_all(user)


async def generate_index(user: User, index: int) -> GenerateResult:
    pass


async def generate_all(user: User) -> GenerateResult:
    pass
