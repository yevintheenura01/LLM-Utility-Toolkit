from pydantic import BaseModel

class TextInput(BaseModel):
    text: str

class QAInput(BaseModel):
    context: str
    question: str
