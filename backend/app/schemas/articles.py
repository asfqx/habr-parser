from pydantic import BaseModel, Field
from typing import Annotated


class BaseArticle(BaseModel):
    title: Annotated[str, Field(..., min_length=1)]
    views: Annotated[str, Field(..., min_length=1)]
    url: Annotated[str, Field(..., min_length=1)]
    text: Annotated[str, Field(..., min_length=1)]


class ResponseSchema(BaseModel):
    status: Annotated[str, Field(..., min_length=1)]
    data: Annotated[list[BaseArticle], Field()]
