from fastapi import FastAPI

# this var contain all the app
app = FastAPI()

# Fast operations
@app.get("/")
def home():
    return {"Hello": "World"}