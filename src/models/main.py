"""Main schema for the Api"""
from pydantic import BaseModel
from uuid import UUID
from enum import Enum


class User(BaseModel):
    uuid: UUID


class Method(str, Enum):
    all = "all"
    index = "index"
