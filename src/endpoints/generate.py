import os
from typing import List

from fastapi import APIRouter

from src.libs.image import save_img, generate_img_index
from src.libs.model import CganCols, get_model
from src.libs.s3 import s3client
from src.models.generate import GenerateResult, ImageResult
from src.models.main import User, Method

IMAGE_STORE_PATH = os.path.abspath("./src/store")
BUCKET_NAME = "pimthaigans-image-container"

# just make sure to have IMAGE_STORE_PATH folder created
if not os.path.exists(IMAGE_STORE_PATH):
    os.makedirs(IMAGE_STORE_PATH)

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

    result: GenerateResult = await generate_all(user)
    return result


async def generate_index(user: User, index: int) -> GenerateResult:
    s3 = s3client()

    output_path = os.path.join(IMAGE_STORE_PATH, f"{user.uuid}-{str(index).zfill(2)}.png")
    used_model = model.model_cols[get_model(index)]
    image = generate_img_index(reloaded_model=used_model, index=index % 11)
    save_img(image, output_path)

    s3_path: str = f"{user.uuid}/{str(index).zfill(2)}.png"
    s3.upload_file(output_path, BUCKET_NAME, s3_path)
    img_url: str = f'https://{BUCKET_NAME}.s3.amazonaws.com/{s3_path}'

    result: List[ImageResult] = [ImageResult(index=index, image_url=img_url)]
    os.remove(output_path)

    s3.close()

    return GenerateResult(user=user, method=Method.index, result=result)


async def generate_all(user: User):
    s3 = s3client()
    result: List[ImageResult] = []

    for index in range(0, 88):
        output_path = os.path.join(IMAGE_STORE_PATH, f"{user.uuid}-{str(index).zfill(2)}.png")
        used_model = model.model_cols[get_model(index)]
        image = generate_img_index(reloaded_model=used_model, index=index % 11)
        save_img(image, output_path)

        s3_path: str = f"{user.uuid}/{str(index).zfill(2)}.png"
        s3.upload_file(output_path, BUCKET_NAME, s3_path)
        image_url = f'https://{BUCKET_NAME}.s3.amazonaws.com/{s3_path}'

        img_detail = ImageResult(index=index,
                                 image_url=image_url)
        result.append(img_detail)

        os.remove(output_path)

    s3.close()

    return GenerateResult(user=user, method=Method.all, result=result)
