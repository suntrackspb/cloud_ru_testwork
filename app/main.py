from fastapi import FastAPI

from routes.routers_info import router as router_info

app = FastAPI(
    title="Cloud.ru API",
    docs_url="/"
)

app.include_router(
    router_info,
    tags=["Information"],
)
