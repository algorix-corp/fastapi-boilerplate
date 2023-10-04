from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from sqlalchemy.exc import DBAPIError
from sqlmodel import SQLModel
from starlette.responses import JSONResponse

from app.utils.database import engine

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.title = "FastAPI-Boilerplate"


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="FastAPI-Boilerplate",
        version="0.0.1",
        summary="Boilerplate",
        description='I am migi',
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://avatars.githubusercontent.com/u/107351649"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


@app.exception_handler(DBAPIError)
async def database_exception_handler(_, __):
    return JSONResponse(
        status_code=500,
        content={
            "detail": "An unexpected database error occurred. Please try again later.",
        },
    )


@app.exception_handler(Exception)
async def exception_handler(_, __):
    return JSONResponse(
        status_code=500,
        content={
            "detail": "An unexpected error occurred. Please try again later.",
        },
    )


@app.on_event("startup")
async def startup():
    # app.include_router(root.router)

    SQLModel.metadata.create_all(engine)

    app.openapi = custom_openapi()


@app.get("/coffee")
def coffee():
    return HTTPException(status_code=418, detail="I'm a teapot")
