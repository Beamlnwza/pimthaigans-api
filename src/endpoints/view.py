from fastapi import APIRouter

from src.libs.s3 import s3resource
from src.models.view import ViewResult, ViewImage
from src.models.main import User, Method
from uuid import UUID

router = APIRouter(
    prefix="/view",
    tags=["View"],
    responses={404: {"description": "Not found"}},
)

BUCKET_NAME = "pimthaigans-image-container"


@router.get("/status")
async def status():
    return {"status": "OK"}


@router.get("/")
async def view(user: UUID, index: int | None = None) -> ViewResult:
    s3 = s3resource()
    bucket = s3.Bucket('pimthaigans-image-container')

    objs = list(bucket.objects.filter(Prefix=f'{user}/'))
    path_objs = [obj.key for obj in objs]

    if len(path_objs) == 0:
        return ViewResult(user=User(uuid=user), method=Method.index, result=None)

    if index or index == 0:
        result: ViewResult = await view_index(User(uuid=user), index, path_objs)
        return result

    result: ViewResult = await view_all(User(uuid=user), path_objs)
    return result


async def view_index(user: User, index: int, path_objs) -> ViewResult:
    imgs = [obj for obj in path_objs if obj.endswith(
        f'{str(index).zfill(2)}.png')]
    if len(imgs) > 0:
        img_url = f'https://{BUCKET_NAME}.s3.amazonaws.com/{imgs[0]}'
        return ViewResult(user=user, method=Method.index, result=[ViewImage(index=index, image_url=img_url)])

    return ViewResult(user=user, method=Method.index, result=None)


async def view_all(user: User, path_objs) -> ViewResult:
    img_urls = []
    for index in range(0, 88):
        imgs = [obj for obj in path_objs if obj.endswith(
            f'{str(index).zfill(2)}.png')]
        if len(imgs) > 0:
            img_urls.append(
                f'https://{BUCKET_NAME}.s3.amazonaws.com/{imgs[0]}')
        else:
            return ViewResult(user=user, method=Method.all, result=None)

    return ViewResult(user=user, method=Method.all,
                      result=[ViewImage(index=index, image_url=img_url) for index, img_url in enumerate(img_urls)])
