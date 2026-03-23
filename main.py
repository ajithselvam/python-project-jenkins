from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def say_hello():
    return {"message": "Hello, Python FastAPI!"}

# To run this locally without Docker:
# uvicorn main:app --reload
