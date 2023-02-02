import os
from fastapi.logger import logger
import sys

import logging
from starlette.middleware.cors import CORSMiddleware

from fastapi import FastAPI, Depends, Request
from fastapi.responses import RedirectResponse, JSONResponse

from config import Settings, get_settings

from website import site, web_config


from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn




log = logging.getLogger("uvicorn")


settings: Settings = get_settings()

# print(settings.debug)
# print(os.getenv("DEBUG"))



origins = [

    # "http://0.0.0.0:5000",
    "*",
]


def create_application() -> FastAPI:
    application = FastAPI()
    application.mount(
        "/static", StaticFiles(directory="./Python/static"), name="static")

    application.include_router(site.router, tags=["site"])
  

    application.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        expose_headers=["*"],

    )
    # set up database

    return application


app = create_application()

if __name__ == "__main__":
    server_port = int(os.environ.get('PORT', 8080))
    uvicorn.run("main:app", host="0.0.0.0", port=server_port, log_level="info")


# app.mount("/static", StaticFiles(directory="./static"), name="static")

# uvicorn --host 127.0.0.1 --port 8000 --workers 4 app.main:create_application --reload --factory
# uvicorn app.main:app --reload
