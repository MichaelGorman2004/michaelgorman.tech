from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.markdown_service import render_markdown

router = APIRouter()


class MarkdownRequest(BaseModel):
    content: str


class MarkdownResponse(BaseModel):
    html: str


@router.post("/render", response_model=MarkdownResponse)
def render_markdown_content(request: MarkdownRequest):
    try:
        html_content = render_markdown(request.content)
        return {"html": html_content}
    except Exception as e:
        raise HTTPException(
            status_code=400, detail=f"Error rendering markdown: {str(e)}"
        )
