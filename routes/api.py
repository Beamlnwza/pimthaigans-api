from fastapi import APIRouter
from src.endpoints import generate, view

router = APIRouter()
router.include_router(generate.router)
router.include_router(view.router)
