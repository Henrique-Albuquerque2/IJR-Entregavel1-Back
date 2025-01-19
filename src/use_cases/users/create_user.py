from fastapi import APIRouter, HTTPException
from repositories.user_repository import UserRepository
from entities.user import User
from utils.auth import hash_password

router = APIRouter()

@router.post("/create-user")
def create_user(user: User):
    try:
        # Hashear a senha antes de salvar
        user.password = hash_password(user.password)

        # Salvar no banco de dados
        new_user = UserRepository.create_user(user.model_dump())
        return {"message": "Usuário criado com sucesso!", "user": new_user.to_json()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao criar usuário: {str(e)}")
