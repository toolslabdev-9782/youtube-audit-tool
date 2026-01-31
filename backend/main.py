from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "OK"}

@app.post("/api/audit/facebook")
def facebook_test(payload: dict):
    return {
        "status": "success",
        "received": payload
    }