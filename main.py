from fastapi import FastAPI

app = FastAPI()

app.get("/")
async def root():
    return {"message": "Application is up and running!"}



