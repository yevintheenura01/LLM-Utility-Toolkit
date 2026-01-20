from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from app.schemas import (
    TextInput,
    QAInput,
    SummarizationInput,
    SummarizationOutput,
    JSONExtractionInput,
    JSONExtractionOutput,
    StructuredDataInput,
    StructuredDataOutput,
    QAOutput
)
from app.llm import (
    summarize_text,
    extract_json,
    answer_question,
    generate_structured_data
)

# Create FastAPI app
app = FastAPI(
    title="LLM Utility Toolkit",
    description="A Python-based toolkit using LLM for common utilities",
    version="1.0.0"
)

# Add CORS middleware for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check endpoint
@app.get("/health")
async def health_check():
    """Check if the API is running."""
    return {"status": "healthy"}

# Text Summarization endpoint
@app.post("/summarize", response_model=SummarizationOutput)
async def summarize(input_data: SummarizationInput):
    """
    Summarize the provided text.
    
    - **text**: The text to summarize
    - **max_length**: Maximum length of the summary (default: 150)
    """
    try:
        result = await summarize_text(input_data.text, input_data.max_length)
        return SummarizationOutput(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error summarizing text: {str(e)}")

# JSON Extraction endpoint
@app.post("/extract-json", response_model=JSONExtractionOutput)
async def extract(input_data: JSONExtractionInput):
    """
    Extract structured JSON data from text.
    
    - **text**: The text to extract data from
    - **schema_description**: Description of the data schema to extract
    """
    try:
        result = await extract_json(input_data.text, input_data.schema_description)
        return JSONExtractionOutput(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error extracting JSON: {str(e)}")

# Question Answering endpoint
@app.post("/answer", response_model=QAOutput)
async def answer(input_data: QAInput):
    """
    Answer a question based on provided context.
    
    - **context**: The context/document to answer from
    - **question**: The question to answer
    """
    try:
        result = await answer_question(input_data.context, input_data.question)
        return QAOutput(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error answering question: {str(e)}")

# Structured Data Generation endpoint
@app.post("/generate-data", response_model=StructuredDataOutput)
async def generate_data(input_data: StructuredDataInput):
    """
    Generate structured data based on description and type.
    
    - **description**: Description of the data to generate
    - **data_type**: Type of data to generate (e.g., "product", "person", "event")
    """
    try:
        result = await generate_structured_data(input_data.description, input_data.data_type)
        return StructuredDataOutput(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating data: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
