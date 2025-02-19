from fastapi import FastAPI

app = FastAPI()

@app.get("/")  # Ensure the decorator is correct
async def root():
    return "Application is up and running!"


@app.get("/Information")
async def info():
    

    return "Information needs to added here"
