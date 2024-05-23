from fastapi import FastAPI
from app.requests.payloads import InputTextBody

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/extracted-name-entities")
async def extract_name_entities(body: InputTextBody):

    return ""