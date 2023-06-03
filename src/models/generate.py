from typing import List
from pydantic import BaseModel
from src.models.main import User, Method


class ImageResult(BaseModel):
    index: int
    image_url: str


class GenerateResult(BaseModel):
    user: User
    method: Method
    result: List[ImageResult]
