from fastapi import APIRouter

from app.api.endpoints import (
    projects,
    experiences,
    messages,
    resume_requests,
    auth,
    markdown,
)

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(projects.router, prefix="/projects", tags=["projects"])
api_router.include_router(
    experiences.router, prefix="/experiences", tags=["experiences"]
)
api_router.include_router(messages.router, prefix="/messages", tags=["messages"])
api_router.include_router(
    resume_requests.router, prefix="/resume-requests", tags=["resume_requests"]
)
api_router.include_router(markdown.router, prefix="/markdown", tags=["markdown"])
