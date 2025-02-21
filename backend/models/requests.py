from pydantic import BaseModel

# Model for accepting strings of text
class TextRequest(BaseModel):
    text: str