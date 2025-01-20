from fastapi import APIRouter, HTTPException
from models.user import UserModel
from utils.auth import verify_password
from utils.jwt import create_access_token
from pydantic import BaseModel

router = APIRouter()

class LoginRequest(BaseModel):
    email: str
    password: str

@router.post("/login")
def login(data: LoginRequest):
    # Verificar se o usuário existe
    user = UserModel.objects(email=data.email).first()
    if not user or not verify_password(data.password, user.password):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    # Gerar o token de acesso
    token = create_access_token({"user_id": str(user.id)})

    # Retornar o token e o nome do usuário
    return {"access_token": token, "user_name": user.username}
