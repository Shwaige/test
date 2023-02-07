from fastapi import FastAPI
from moble import Iemt

app = FastAPI()


def add(a, b):
    return a + b


@app.get("/")  # 接口
def index():
    return {"msg": "hello"}


@app.get("/get")
def app_get(a: int, b: int):
    c = add(a, b)
    return {"c": c}


@app.post("/post")
def app_post(inmt: Iemt):
    c = add(inmt.a, inmt.b)
    return {"c": c}
