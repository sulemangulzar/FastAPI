from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from database import get_session
from models import Todo
from schemas import TodoCreate, TodoRead, TodoUpdate

router = APIRouter()


@router.get("/todos", response_model=list[TodoRead])
def get_todos(session: Session = Depends(get_session)):
    todos = session.exec(select(Todo)).all()
    return todos


@router.get("/todos/{todo_id}", response_model=TodoRead)
def get_todo(todo_id: int, session: Session = Depends(get_session)):
    todo = session.get(Todo, todo_id)

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    return todo


@router.post("/todos", response_model=TodoRead)
def create_todo(todo_data: TodoCreate, session: Session = Depends(get_session)):
    todo = Todo(**todo_data.model_dump())

    session.add(todo)
    session.commit()
    session.refresh(todo)

    return todo


@router.put("/todos/{todo_id}", response_model=TodoRead)
def update_todo(
    todo_id: int, todo_data: TodoUpdate, session: Session = Depends(get_session)
):
    todo = session.get(Todo, todo_id)

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    update_data = todo_data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(todo, key, value)

    session.add(todo)
    session.commit()
    session.refresh(todo)

    return todo


@router.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, session: Session = Depends(get_session)):
    todo = session.get(Todo, todo_id)

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    session.delete(todo)
    session.commit()

    return {"message": "Todo deleted successfully"}
