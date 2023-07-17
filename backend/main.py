from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
  data = {
    "message": "hello"
  }
  return data