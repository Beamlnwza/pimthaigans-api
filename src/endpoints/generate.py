from fastapi import APIRouter
import os
from src.libs.model import CganCols, get_model
from src.models.main import User, Method
from src.models.generate import GenerateResult, ImageResult
from src.libs.s3 import s3client
from src.libs.image import save_img, generate_img_index

IMAGE_STORE_PATH = os.path.abspath("./src/store")
BUCKET_NAME = "pimthaigans-image-container"

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


async def generate_index(user: User, index: int) -> GenerateResult:
    s3 = s3client()
    output_path = os.path.join(IMAGE_STORE_PATH, f"{user.uuid}-{str(index).zfill(2)}.png")
    used_model = model.model_cols[get_model(index)]
    image = generate_img_index(reloaded_model=used_model, index=index % 11)
    save_img(image, output_path)
    s3_path = f"{user.uuid}/{str(index).zfill(2)}.png"
    s3.upload_file(output_path, BUCKET_NAME, s3_path)
    img_url = f'https://{BUCKET_NAME}.s3.amazonaws.com/{s3_path}'
    os.remove(output_path)
    s3.close()

    return GenerateResult(user=user, method=Method.index, result=[ImageResult(index=index, image_url=img_url)])


# async def generate_all(user: User) -> GenerateResult:
#     s3 = await s3client()
#     for index in range(0, 88):
#         output_path = os.path.join(IMAGE_STORE_PATH, f"{user.uuid}-{str(index).zfill(2)}.png")
#         image = await generate_index(index=index, reloaded_model=model.model_cols[0])
#         await save_img(image, output_path)
#     await s3.close()
#     pass
