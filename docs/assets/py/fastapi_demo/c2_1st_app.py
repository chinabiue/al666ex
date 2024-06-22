from fastapi import FastAPI  # (1)!

app = FastAPI()  # (2)!


@app.get("/")  # (3)!
async def home():
    return {"message": "Hello, World!"}
