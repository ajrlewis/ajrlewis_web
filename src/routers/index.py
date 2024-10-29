from typing import Annotated

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from loguru import logger

from ..dependencies import GetDBDep, GetCurrentUserDep


templates = Jinja2Templates(directory="templates/")

router = APIRouter(prefix="")


@router.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


# @router.get("/ping")
# async def ping(db: GetDBDep, user: GetCurrentUserDep):
#     logger.debug(f"{user = }")
#     try:
#         _ = db.connection()
#     except Exception as e:
#         raise HTTPException(status_code=400, detail="Database unavailable")
#     return {"message": "Pong"}
