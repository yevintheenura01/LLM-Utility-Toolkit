# LLM-Utility-Toolkit

A Python-based toolkit that uses OpenAI's LLM to perform common utilities exposed via a REST API.

## 🎯 Features

- **Text Summarization** - Summarize long texts to key points
- **JSON Extraction** - Extract structured data from unstructured text
- **Question Answering** - Answer questions based on provided context
- **Structured Data Generation** - Generate realistic structured data examples

## 🧠 What This Project Demonstrates

✅ LLM understanding and prompt engineering  
✅ OpenAI API integration  
✅ Structured outputs with Pydantic  
✅ REST API design with FastAPI  
✅ Async/Await patterns in Python  
✅ JSON handling and validation  
✅ Environment variable management with dotenv

## 🛠️ Tech Stack

- **Python 3.8+**
- **FastAPI** - Modern web framework for building APIs
- **OpenAI API** - GPT-4o-mini model for LLM capabilities
- **Pydantic** - Data validation using Python type annotations
- **Uvicorn** - ASGI web server
- **python-dotenv** - Environment variable management

## 📋 Prerequisites

- Python 3.8 or higher
- OpenAI API key (get one at https://platform.openai.com/api-keys)

## 🚀 Installation

1. **Clone the repository**

```bash
git clone https://github.com/yevintheenura01/LLM-Utility-Toolkit.git
cd LLM-Utility-Toolkit
```

2. **Create a virtual environment**

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up environment variables**

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env and add your OpenAI API key
# OPENAI_API_KEY=your-api-key-here
```

## 🏃 Running the Application

Start the API server:

```bash
python -m app.main
```

The API will be available at `http://localhost:8000`

**Interactive API Documentation:**

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 📡 API Endpoints

### Health Check

```
GET /health
```

Check if the API is running.

### Text Summarization

```
POST /summarize
```

Summarize the provided text.

**Request Body:**

```json
{
  "text": "Your long text here...",
  "max_length": 150
}
```

**Response:**

```json
{
  "summary": "Summarized version...",
  "original_length": 1000,
  "summary_length": 150
}
```

### JSON Extraction

```
POST /extract-json
```

Extract structured JSON data from unstructured text.

**Request Body:**

```json
{
  "text": "John is 30 years old and works at Acme Corp.",
  "schema_description": "Extract person information with fields: name, age, company"
}
```

**Response:**

```json
{
  "data": {
    "name": "John",
    "age": 30,
    "company": "Acme Corp"
  },
  "success": true,
  "error": null
}
```

### Question Answering

```
POST /answer
```

Answer a question based on provided context.

**Request Body:**

```json
{
  "context": "Python is a high-level programming language...",
  "question": "What is Python?"
}
```

**Response:**

```json
{
  "answer": "Python is a high-level programming language known for its simplicity...",
  "confidence": "high"
}
```

### Structured Data Generation

```
POST /generate-data
```

Generate realistic structured data based on description and type.

**Request Body:**

```json
{
  "description": "An e-commerce product with title, price, and rating",
  "data_type": "product"
}
```

**Response:**

```json
{
  "data": {
    "title": "Wireless Bluetooth Headphones",
    "price": 79.99,
    "rating": 4.5,
    "category": "Electronics"
  },
  "schema_used": "product"
}
```

## 📁 Project Structure

```
LLM-Utility-Toolkit/
├── app/
│   ├── __init__.py          # Package initialization
│   ├── main.py              # FastAPI application and endpoints
│   ├── llm.py               # LLM service functions (async)
│   ├── schemas.py           # Pydantic models for request/response
│   └── config.py            # Configuration management
├── .env.example             # Example environment variables
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## 🔑 Key Concepts

### Async/Await

The LLM functions use Python's async/await to handle I/O-bound operations (API calls) without blocking.

```python
async def ask_llm(prompt: str) -> str:
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None, lambda: ...)
```

### Pydantic Models

Input and output validation using Pydantic ensures type safety and automatic documentation.

```python
class SummarizationInput(BaseModel):
    text: str
    max_length: Optional[int] = 150
```

### Environment Variables

Sensitive data like API keys are managed through `.env` files using `python-dotenv`.

## 🤖 LLM Model

This project uses **gpt-4o-mini** by default. You can change the model by:

1. Updating the `OPENAI_MODEL` variable in `.env`
2. Passing the model parameter to LLM functions

Available models: `gpt-4o`, `gpt-4o-mini`, `gpt-3.5-turbo`

## 🧪 Testing the API

### Using cURL:

```bash
curl -X POST "http://localhost:8000/summarize" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "This is a long text that needs to be summarized. It contains multiple sentences with important information...",
    "max_length": 50
  }'
```

### Using Python requests:

```python
import requests

response = requests.post(
    "http://localhost:8000/summarize",
    json={
        "text": "Your text here...",
        "max_length": 100
    }
)
print(response.json())
```

## ⚙️ Configuration

Edit the `.env` file to configure:

```env
# OpenAI Configuration
OPENAI_API_KEY=your-api-key-here
OPENAI_MODEL=gpt-4o-mini

# API Configuration
API_HOST=0.0.0.0
API_PORT=8000
```

## 🐛 Troubleshooting

**Error: "OPENAI_API_KEY environment variable is not set"**

- Make sure you've copied `.env.example` to `.env`
- Add your actual OpenAI API key to the `.env` file

**Error: "Invalid API key"**

- Check that your OpenAI API key is correct
- Make sure the key has appropriate permissions

**Error: "Connection refused"**

- Make sure the API server is running
- Check that port 8000 is not in use

## 📚 Learning Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [OpenAI API Documentation](https://platform.openai.com/docs/api-reference)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Python AsyncIO](https://docs.python.org/3/library/asyncio.html)

## 📝 License

MIT License - feel free to use this project for learning and development.

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

---

**Happy coding! 🚀**
