# ==========================================
# Candidate Management API
# ==========================================
#
# Instructions to run:
# 1. Install dependencies: pip install fastapi pydantic[email] uvicorn
# 2. Run the application using uvicorn:
#    uvicorn main:app --reload
#
# The API documentation will be available at: http://127.0.0.1:8000/docs
# ==========================================

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional, Dict
from enum import Enum
import uuid

# --- Enums ---
class CandidateStatus(str, Enum):
    applied = "applied"
    interview = "interview"
    selected = "selected"
    rejected = "rejected"

# --- Models ---
class CandidateCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, description="Name of the candidate")
    email: EmailStr = Field(..., description="Email address of the candidate")
    skill: str = Field(..., min_length=1, max_length=100, description="Primary skill of the candidate")
    status: CandidateStatus = Field(default=CandidateStatus.applied, description="Current status of the candidate")

class CandidateUpdateStatus(BaseModel):
    status: CandidateStatus = Field(..., description="New status to apply")

class CandidateResponse(BaseModel):
    id: str = Field(..., description="Unique ID of the candidate")
    name: str = Field(..., description="Name of the candidate")
    email: EmailStr = Field(..., description="Email address of the candidate")
    skill: str = Field(..., description="Primary skill of the candidate")
    status: CandidateStatus = Field(..., description="Current status of the candidate")

# --- FastAPI Initialization ---
app = FastAPI(
    title="Candidate Management API",
    description="A simple backend API to manage candidates for a recruitment system.",
    version="1.0.0"
)

# --- In-Memory Storage ---
# Dictionary mapping candidate ID to CandidateResponse objects
candidates_db: Dict[str, CandidateResponse] = {}

# --- API Endpoints ---

@app.post("/candidates", response_model=CandidateResponse, status_code=201, summary="Create a new candidate")
def create_candidate(candidate: CandidateCreate):
    """
    Add a new candidate to the system.
    """
    # Auto-generate unique ID
    candidate_id = str(uuid.uuid4())
    
    new_candidate = CandidateResponse(
        id=candidate_id,
        name=candidate.name,
        email=candidate.email,
        skill=candidate.skill,
        status=candidate.status
    )
    
    candidates_db[candidate_id] = new_candidate
    return new_candidate

@app.get("/candidates", response_model=List[CandidateResponse], summary="Get all candidates")
def get_all_candidates(status: Optional[CandidateStatus] = Query(None, description="Filter candidates by status")):
    """
    Retrieve a list of all candidates. 
    Optional: support filtering by status using a query parameter.
    """
    if status:
        return [candidate for candidate in candidates_db.values() if candidate.status == status]
    
    return list(candidates_db.values())

@app.put("/candidates/{id}/status", response_model=CandidateResponse, summary="Update candidate status")
def update_candidate_status(id: str, status_update: CandidateUpdateStatus):
    """
    Update the status of a specific candidate by ID.
    """
    if id not in candidates_db:
        # Proper error handling
        raise HTTPException(status_code=404, detail=f"Candidate with ID '{id}' not found")
    
    # Update candidate status
    candidate = candidates_db[id]
    candidate.status = status_update.status
    
    # Optional: can trigger actions like saving to persistent DB here
    
    return candidate
