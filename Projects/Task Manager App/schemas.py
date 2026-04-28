from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    description: str
    priority: str
    
class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    priority: str
    status: str
    
class UpdateStatus(BaseModel):
    status: str
    
class MessageResponse(BaseModel):
    message: str