import uvicorn

from fastapi import FastAPI
from auth_app.auth_api import auth_router

app = FastAPI()

@app.get("/")
async def root():
    return {"Hello": "world!"}

app.include_router(auth_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
