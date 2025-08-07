# AI-Powered Validation Function Generator

This system uses Claude 3.7 LLM to generate JavaScript validation functions for educational activities. It includes a meta-validation engine to verify function correctness and provides pedagogically appropriate feedback to students.

## Features

- **Function Generation**: Dynamically generates JavaScript validation functions using Claude 3.7
- **Meta-Validation Engine**: Tests generated functions for correctness and reliability
- **Feedback Engine**: Generates context-aware feedback for student responses
- **Template Library**: Reusable validation patterns for common scenarios
- **Test Suite Generator**: Creates comprehensive test cases for validation
- **Error Handling Framework**: Robust error detection and classification
- **Adaptive Feedback Loop**: Continuously improves prompts based on performance

## Architecture

- **Backend**: FastAPI with LangChain components
- **Frontend**: React with Material-UI
- **LLM**: Claude 3.7 via Anthropic API
- **JS Execution**: PyMiniRacer for sandboxed JavaScript validation
- **Monitoring**: LangSmith for tracing and debugging

## Setup Instructions

### Prerequisites

- Python 3.8+
- Node.js 14+
- Anthropic API key
- LangSmith API key (optional, for tracing)

### Backend Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   ```bash
   # Create .env file
   echo "ANTHROPIC_API_KEY=your-api-key" > .env
   echo "LANGCHAIN_API_KEY=your-langsmith-api-key" >> .env
   echo "LANGCHAIN_TRACING_V2=true" >> .env
   echo "LANGCHAIN_PROJECT=validation-function-generator" >> .env
   ```

4. Run the backend:
   ```bash
   cd backend
   uvicorn main:app --reload
   ```

### Frontend Setup

1. Install dependencies:
   ```bash
   cd frontend
   npm install
   ```

2. Run the frontend:
   ```bash
   npm start
   ```

## Usage

1. **Create Activity**: Define an activity with description and expected answer
2. **Generate Validation Function**: The system will create a JavaScript function to validate student responses
3. **Test Validation**: Run test cases against the validation function
4. **Test Feedback**: See how the system responds to different student answers

## API Endpoints

- `POST /generate-validation`: Generate a validation function for an activity
- `POST /validate-answer`: Validate a student's answer and provide feedback
- `POST /test-validation`: Test a validation function against test cases
- `POST /improve-prompts`: Trigger an adaptive improvement cycle
- `GET /health`: Health check endpoint

## Project Structure

```
.
├── backend/
│   ├── main.py              # FastAPI application
│   ├── api.py               # API endpoints
│   ├── templates.py         # Validation function templates
│   ├── test_generator.py    # Test case generation
│   ├── error_handling.py    # Error handling framework
│   └── adaptive_loop.py     # Adaptive feedback loop
├── frontend/
│   ├── public/
│   └── src/
│       ├── components/      # Reusable UI components
│       ├── pages/           # Application pages
│       └── App.js           # Main application component
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## License

This project is licensed under the MIT License.