from app.services.article_service import get_articles_from_habr
from app.web.utils import json_response
from app.schemas.articles import ResponseSchema
from fastapi import APIRouter
from dataclasses import asdict

router = APIRouter()


@router.get("/top_habr", response_model=ResponseSchema)
async def get_top_habr():
    data = [asdict(article) for article in await get_articles_from_habr()]
    return json_response(data=data)
