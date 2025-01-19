from fastapi import APIRouter, HTTPException, Depends
from repositories.task_repository import TaskRepository
from middlewares.auth import get_current_user

router = APIRouter()

@router.delete("/tasks/{id}")
def delete_task(id: str, user_id: str = Depends(get_current_user)):
    try:
        success = TaskRepository.delete_task(id, user_id)
        if not success:
            raise HTTPException(status_code=404, detail="Tarefa não encontrada ou você não tem permissão para deletá-la")
        return {"message": "Tarefa deletada com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao deletar tarefa: {str(e)}")
