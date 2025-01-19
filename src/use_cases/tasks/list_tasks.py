from fastapi import APIRouter, HTTPException, Depends
from repositories.task_repository import TaskRepository
from middlewares.auth import get_current_user

router = APIRouter()

@router.get("/tasks")
def list_tasks(user_id: str = Depends(get_current_user)):
    try:
        tasks = TaskRepository.get_all_tasks_by_user(user_id)
        return {"tasks": [task.to_json() for task in tasks]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao listar tarefas: {str(e)}")
