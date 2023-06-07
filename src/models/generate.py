from typing import List
from src.models.main import User, Method
from pydantic import BaseModel, HttpUrl


class ImageResult(BaseModel):
    index: int
    image_url: HttpUrl


class GenerateResult(BaseModel):
    user: User
    method: Method
    result: List[ImageResult]
