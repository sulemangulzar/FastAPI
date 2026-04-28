from fastapi import FastAPI,HTTPException
from schemas import TaskCreate, TaskResponse, UpdateStatus, MessageResponse
from database import Database

app = FastAPI()
db = Database()
db.connect_to_db()


@app.get("/tasks", response_model=list[TaskResponse])
def get_all_tasks():
    try:
        result = db.get_all_tasks()
        if result:
            return result
        raise HTTPException(status_code=404, detail="Not Found")
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))
    
    
    
@app.post("/create", response_model=TaskResponse)
def create_note(task: TaskCreate):
    task_id = db.create_task(task)
    
    data = task.model_dump()
    data["status"] = "Not Completed"

    return {
        "id": task_id,
        **data
    }


@app.get("/task/{id}", response_model=TaskResponse)
def get_task(id: int):
    try:
        result = db.get_task(id)
        if result:
            return result
        raise HTTPException(status_code=404, detail="Not Found")
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))
    
@app.put("/update_status/{task_id}", response_model=TaskResponse)
def update_status(task_id: int, data: UpdateStatus):
    try:
        updated = db.update_status(data.status, task_id)
        if not updated:
            raise HTTPException(status_code=404, detail="Task not found")

        return db.get_task(task_id)

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))
    
@app.delete("/task/{id}", response_model=MessageResponse)
def delete_task(id: int):
    try:
        result = db.delete_task(id)
        if result:
            return {"message" : "Deleted"}
        raise HTTPException(status_code=404, detail="Not Found")
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))