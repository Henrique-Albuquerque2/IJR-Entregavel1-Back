# src/use_cases/register_user.py
from repositories.user_repository import UserRepository
from bcrypt import hashpw, gensalt

def register_user(data: dict):
    data["password"] = hashpw(data["password"].encode(), gensalt())
    return UserRepository.create_user(data)
