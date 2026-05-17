from pydantic import BaseModel


class TodoCreate(BaseModel):
    title: str
    completed: bool = False


class TodoRead(BaseModel):
    id: int
    title: str
    completed: bool


class TodoUpdate(BaseModel):
    title: str
    completed: bool
