from fastapi import APIRouter, HTTPException, Depends
from repositories.task_repository import TaskRepository
from middlewares.auth import get_current_user

router = APIRouter()

@router.get("/tasks")
def list_tasks(user_id: str = Depends(get_current_user)):
    try:
        tasks = TaskRepository.get_all_tasks_by_user(user_id)

        # Serializa as tarefas para converter `_id` em string
        def format_task(task):
            task_json = task.to_json()
            task_json["_id"] = str(task.id)  # Converte o ObjectId para string
            return task_json

        return {"tasks": [format_task(task) for task in tasks]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao listar tarefas: {str(e)}")
