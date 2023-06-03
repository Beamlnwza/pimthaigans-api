from typing import List

from pydantic import BaseModel

from src.models.main import User, Method


class ViewImage(BaseModel):
    index: int
    image_url: str

class ViewResult(BaseModel):
    user: User
    method: Method
    result: List[ViewImage] | None