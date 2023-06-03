from fastapi import APIRouter

from src.libs.s3 import s3resource
from uuid import UUID

router = APIRouter(
    prefix="/view",
    tags=["View"],
    responses={404: {"description": "Not found"}},
)


@router.get("/status")
async def status():
    return {"status": "OK"}


@router.get("/")
async def view(user: UUID, index: int | None = None):
    s3 = s3resource()
    bucket = s3.Bucket('pimthaigans-image-container')
    objs = list(bucket.objects.filter(Prefix=f'{user}/'))
    if index:
        return objs[index].key
    return [obj.key for obj in objs]
