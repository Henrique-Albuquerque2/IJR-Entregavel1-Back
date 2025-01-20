from fastapi import APIRouter, Depends, HTTPException, Header
from utils.jwt import decode_access_token
from models.task import TaskModel

router = APIRouter()

@router.get("/tasks/summary")
def get_task_summary(authorization: str = Header(...)):
    # Verifica se o cabeçalho Authorization está no formato correto
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Token ausente ou em formato inválido")

    # Remove o prefixo "Bearer " para obter o token
    token = authorization.split(" ")[1]

    # Tenta decodificar o token
    try:
        decoded_token = decode_access_token(token)
    except Exception as e:
        raise HTTPException(status_code=401, detail=f"Erro ao decodificar o token: {str(e)}")

    # Obtém o user_id do token decodificado
    user_id = decoded_token.get("user_id")
    if not user_id:
        raise HTTPException(status_code=401, detail="Token inválido: user_id ausente")

    # Filtra as tarefas do usuário
    try:
        tasks = TaskModel.objects(owner=user_id)
        summary = {
            "finalizada": tasks.filter(status="finalizada").count(),
            "emProgresso": tasks.filter(status="emProgresso").count(),
            "pendente": tasks.filter(status="pendente").count(),
        }
        return summary
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar tarefas: {str(e)}")
