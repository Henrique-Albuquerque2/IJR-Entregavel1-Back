from fastapi import APIRouter, HTTPException, Depends
from entities.task import Task
from repositories.task_repository import TaskRepository
from middlewares.auth import get_current_user

router = APIRouter()

@router.put("/tasks/{id}")
def update_task(id: str, task: Task, user_id: str = Depends(get_current_user)):
    try:
        updated_task = TaskRepository.update_task(id, task.dict(), user_id)
        if not updated_task:
            raise HTTPException(status_code=404, detail="Tarefa não encontrada ou você não tem permissão para atualizá-la")
        return {"message": "Tarefa atualizada com sucesso!", "task": updated_task.to_json()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao atualizar tarefa: {str(e)}")
