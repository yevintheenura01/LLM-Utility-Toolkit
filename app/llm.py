from openai import OpenAI
import os
import json
import asyncio
from typing import Any

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def ask_llm(prompt: str, model: str = "gpt-4o-mini") -> str:
    """
    Send a prompt to OpenAI and get a response asynchronously.
    """
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(
        None,
        lambda: client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
    )
    return response.choices[0].message.content

async def summarize_text(text: str, max_length: int = 150, model: str = "gpt-4o-mini") -> dict[str, Any]:
    """
    Summarize text using LLM.
    """
    prompt = f"""Summarize the following text in approximately {max_length} words or less.
    
Text:
{text}

Provide only the summary, nothing else."""
    
    summary = await ask_llm(prompt, model)
    
    return {
        "summary": summary,
        "original_length": len(text),
        "summary_length": len(summary)
    }

async def extract_json(text: str, schema_description: str, model: str = "gpt-4o-mini") -> dict[str, Any]:
    """
    Extract structured JSON data from text using LLM.
    """
    prompt = f"""Extract the following information from the text and return it as valid JSON.

Schema requirements:
{schema_description}

Text:
{text}

Return ONLY valid JSON, no additional text."""
    
    try:
        response = await ask_llm(prompt, model)
        # Try to parse JSON
        data = json.loads(response)
        return {
            "data": data,
            "success": True,
            "error": None
        }
    except json.JSONDecodeError as e:
        return {
            "data": {},
            "success": False,
            "error": f"Failed to parse JSON: {str(e)}"
        }

async def answer_question(context: str, question: str, model: str = "gpt-4o-mini") -> dict[str, Any]:
    """
    Answer a question based on provided context.
    """
    prompt = f"""Based on the following context, answer the question.

Context:
{context}

Question:
{question}

Provide a clear and concise answer."""
    
    answer = await ask_llm(prompt, model)
    
    return {
        "answer": answer,
        "confidence": "high"  # Could be enhanced with more sophisticated confidence scoring
    }

async def generate_structured_data(description: str, data_type: str, model: str = "gpt-4o-mini") -> dict[str, Any]:
    """
    Generate structured data based on a description and data type.
    """
    prompt = f"""Generate a realistic example of a {data_type} with the following characteristics:
{description}

Return as valid JSON with appropriate fields for a {data_type}. Include all relevant fields.
Return ONLY valid JSON, no additional text."""
    
    try:
        response = await ask_llm(prompt, model)
        data = json.loads(response)
        return {
            "data": data,
            "schema_used": data_type
        }
    except json.JSONDecodeError as e:
        return {
            "data": {},
            "schema_used": data_type,
            "error": f"Failed to parse JSON: {str(e)}"
        }
