# Candidate Management API

A simple backend API built with **Python** and **FastAPI** to manage candidates for a recruitment system. This project allows recruiters to add candidates, view a list of all candidates with optional status filtering, and update a candidate's status.

## 🚀 Features

- **Create Candidate**: Add new candidate details (assigned a unique auto-generated UUID).
- **Get All Candidates**: Retrieve lists of candidates, optionally filtering by their current status.
- **Update Candidate Status**: Update an existing candidate's progress status.
- **In-Memory Storage**: Lightweight local data preservation during a single run session.
- **Robust Validation**: Enforces exact Enum statuses and strictly validates email formats using Pydantic.

## 🛠️ Technology Stack

- **Python 3.8+**
- **FastAPI**: A modern, fast, high-performance web framework for building APIs.
- **Pydantic**: Data validation and settings management using Python type hints.
- **Uvicorn**: An ASGI web server implementation for FastAPI.

## ⚙️ Setup & Installation

Follow these steps to set up the project locally:

1. **Navigate to the project directory** (where `main.py` is present):
   ```bash
   cd b:\teak_leap_assignment
   ```

2. **(Optional) Create a virtual environment** to isolate dependencies:
   ```bash
   python -m venv venv
   
   # Activate on Windows:
   venv\Scripts\activate
   
   # Activate on macOS/Linux:
   source venv/bin/activate
   ```

3. **Install the required packages**:
   Using the provided `requirements.txt` file, install the project dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   *(If you aren't using `requirements.txt`, manually run: `pip install fastapi "pydantic[email]" uvicorn`)*

## 🚦 How to Run

1. Start the local server using `uvicorn`:
   ```bash
   uvicorn main:app --reload
   ```
   *The `--reload` flag enables auto-reloading whenever you make changes to the code.*

2. Your server will start running at:  `http://127.0.0.1:8000`

### Interactive API Documentation
FastAPI automatically generates an interactive Swagger documentation page. Open your browser and navigate to:
👉 **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**


## 🔗 API Reference

### 1. Create a Candidate
- **Endpoint**: `POST /candidates`
- **Description**: Add a new candidate to the system.
- **Request Body** (JSON):
  ```json
  {
      "name": "John Doe",
      "email": "john.doe@example.com",
      "skill": "Python",
      "status": "applied"
  }
  ```
- **Valid Statuses**: `applied`, `interview`, `selected`, `rejected`

### 2. Get All Candidates
- **Endpoint**: `GET /candidates`
- **Description**: Retrieve a list of all candidates. Includes an optional query parameter for filtering.
- **Query Parameter (Optional)**:
  - `status`: Filter list by candidate status (e.g., `GET /candidates?status=interview`)
- **Response**: List of candidate objects containing their tracking IDs.

### 3. Update Candidate Status
- **Endpoint**: `PUT /candidates/{id}/status`
- **Description**: Update the status string of a specific candidate by passing their unique `id`.
- **Request Body** (JSON):
  ```json
  {
      "status": "interview"
  }
  ```
- **Error Types**: Returns `404 Not Found` if a candidate using that specific unique ID doesn't exist.
