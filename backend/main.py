from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Create FastAPI app
app = FastAPI()

# Allow frontend requests (adjust port if using a different one)
origins = [
    "http://localhost:5173",  # Vite
    "http://localhost:8080",  # Create React App (CRA)
]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       # Allow your frontend's origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model
class MessageRequest(BaseModel):
    message: str

# Response model (optional, but good for docs)
class MessageResponse(BaseModel):
    response: str

# POST /chat endpoint
@app.post("/chat", response_model=MessageResponse)
async def echo_message(payload: MessageRequest):
    print(payload.message)
    return {"response": payload.message}
