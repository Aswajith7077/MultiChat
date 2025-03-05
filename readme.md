# FastAPI Project

## Overview
This is a FastAPI-based application designed to provide high-performance APIs using Python. FastAPI is a modern web framework that allows rapid development with automatic interactive API documentation.

## Features
- Fast and lightweight
- Automatic OpenAPI and Swagger documentation
- Asynchronous support
- Dependency injection
- Pydantic for data validation

## Requirements
Ensure you have the following installed:
- Python 3.8+
- FastAPI
- Uvicorn

## Installation

1. Clone the repository:
   ```sh
   git clone <repository_url>
   cd <project_directory>
   ```

2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Running the Server

To start the FastAPI application, run:
```sh
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

- The `--reload` flag enables automatic reloading when code changes.
- The app will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- API documentation:
  - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
  - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Directory Structure
```
project_directory/
│── main.py          # Entry point of the application
│── requirements.txt # Dependencies list
│── .env             # Environment variables (optional)

| --Schema              # Schema definition of the database
| --RequestSchema       # All the Models for API Requests
| -- Config             # Contains a file for dotenv
│── README.md        # Documentation
```

## Creating an API Endpoint

Example `main.py` file:
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
```

# Scripts

These Scripts are not required for the actual server, but just to insert values into the database.

Notice the scripts are runned sequentially in the given order




insertModels.py -> Insert Values into Models Table

insertResponses.py -> Insert Values into Responses Table

insertRegex.py -> Insert Values into Redirection Table

insertFileRedirects.py -> Insert Values into FileRedirection Table

# Docker building 

```bash
docker build -t multichat .
```


```bash
docker run -d --name multichat -p 80:80 --env-file .env multichat
```