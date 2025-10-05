from app.api.article_from_habr import router as habr_router
from fastapi import APIRouter

router = APIRouter(prefix="/api")

router.include_router(habr_router)
