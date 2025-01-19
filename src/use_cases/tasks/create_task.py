from fastapi import APIRouter, HTTPException, Depends
from entities.task import Task
from repositories.task_repository import TaskRepository
from middlewares.auth import get_current_user

router = APIRouter()

@router.post("/tasks")
def create_task(task: Task, user_id: str = Depends(get_current_user)):
    try:
        # Adicionar o ID do usuário como o dono da tarefa
        task_data = task.model_dump()
        task_data["owner"] = user_id

        # Salvar a tarefa no banco de dados
        new_task = TaskRepository.create_task(task_data)
        return {"message": "Tarefa criada com sucesso!", "task": new_task.to_json()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao criar tarefa: {str(e)}")
