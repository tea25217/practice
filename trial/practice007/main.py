from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


class Params(BaseModel):
    text: Union[str, None] = None
    key: Union[str, None] = None


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hoge")
async def hoge():
    return {"message": "fuga"}


@app.post("/")
async def post():
    return {"message": "This is post"}


@app.post("/translate/")
async def translate(params: Params):
    return {"message": "Successfully translated"}


@app.post("/usage/")
async def usage(params: Params):
    return {"message": "Checking usage"}
