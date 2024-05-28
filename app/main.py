from fastapi import FastAPI
from app.requests.payloads import InputTextBody
from app.responses.common_responses import GlobalResponse
from app.spacy.name_extraction import make_html_with_extracted_names_from_input_text
app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "Server is running..."}

@app.post("/extracted-name-entities")
async def extract_name_entities(body: InputTextBody):

    return GlobalResponse(
        message="Name entities are extracted successfully"
        data=make_html_with_extracted_names_from_input_text(body)
    )