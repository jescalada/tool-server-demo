from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from auth import verify_jwt


app = FastAPI(
    title="Echo Tool Server",
    version="1.0.0",
    description="A sample tool server that echoes messages."
)

# Allow all for testing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class EchoInput(BaseModel):
    message: str

class EchoOutput(BaseModel):
    echoed_message: str

@app.post(
    "/tools/echo",
    response_model=EchoOutput,
    tags=["tools"],
    summary="Echo a message",
    description="Echo a message back to the user."
)
def echo_tool(input: EchoInput, user=Depends(verify_jwt)):
    return {"echoed_message": f"Hello, {user.get('name', 'stranger')}! You said: {input.message}"}
