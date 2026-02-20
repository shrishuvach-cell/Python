from fastapi import FastAPI
from pydantic import BaseModel

# Initialize the FastAPI app
app = FastAPI(title="My Python Microservice")

# --- YOUR EXISTING PYTHON CODE ---
def process_data(input_text: str) -> str:
    # Imagine complex logic here (machine learning, data parsing, etc.)
    return input_text.upper() + " (Processed)"
# ---------------------------------

# Define the expected input data structure
class InputData(BaseModel):
    text: str

# Create a Health Check endpoint (crucial for microservices)
@app.get("/health")
def health_check():
    return {"status": "healthy"}

# Create the endpoint that triggers your code
@app.post("/api/run")
def run_my_code(data: InputData):
    result = process_data(data.text)
    return {"original": data.text, "result": result}