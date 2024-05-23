from fastapi import FastAPI
from app.requests.payloads import InputTextBody
from app.responses.common_responses import GlobalResponse

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "Server is running..."}

@app.post("/extracted-name-entities")
async def extract_name_entities(body: InputTextBody):

    return GlobalResponse(
        message="Name entities are extracted successfully"
    )