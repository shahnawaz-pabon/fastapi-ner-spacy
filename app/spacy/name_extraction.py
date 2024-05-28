from fastapi import Body
from spacy import displacy
from typing import List
from .models import get_model
from .clean_text import text_cleaner, text_formatter

model = get_model()


def make_html_with_extracted_names_from_input_text(input_text: str) -> str:

    
    doc = model(text_formatter(input_text))
    options = {"ents": ["ORG", "PERSON", "GPE",
                        "PRODUCT", "DATE", "TIME", "MONEY"]}
    html = displacy.render(doc, options=options, style='ent')
    
    return html