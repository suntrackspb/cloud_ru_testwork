import os
import platform

from fastapi import APIRouter

router = APIRouter()


@router.get(
    "/author",
    summary="Get project author",
)
async def get_author():
    """Return author name"""
    return os.getenv("AUTHOR")


@router.get(
    "/hostname",
    summary="Get current hostname",
)
async def get_author():
    """Return current hostname"""
    return platform.node()


@router.get("/id", summary="Get UUID")
@router.get("/uuid", summary="Get UUID")
async def get_author():
    """Return UUID"""
    return os.getenv("UUID")
