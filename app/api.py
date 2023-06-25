from fastapi import FastAPI

black76 = FastAPI()


@black76.get("/")
async def root():
    return {"message": "Hello World"}
