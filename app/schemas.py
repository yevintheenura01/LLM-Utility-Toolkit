from pydantic import BaseModel
from typing import Any, Optional

# Input schemas
class TextInput(BaseModel):
    text: str

class QAInput(BaseModel):
    context: str
    question: str

class SummarizationInput(BaseModel):
    text: str
    max_length: Optional[int] = 150

class JSONExtractionInput(BaseModel):
    text: str
    schema_description: str

class StructuredDataInput(BaseModel):
    description: str
    data_type: str  # e.g., "product", "person", "event"

# Output schemas
class SummarizationOutput(BaseModel):
    summary: str
    original_length: int
    summary_length: int

class JSONExtractionOutput(BaseModel):
    data: dict[str, Any]
    success: bool
    error: Optional[str] = None

class QAOutput(BaseModel):
    answer: str
    confidence: Optional[str] = None

class StructuredDataOutput(BaseModel):
    data: dict[str, Any]
    schema_used: str
