# src/repositories/user_repository.py
from models.user import UserModel

class UserRepository:
    @staticmethod
    def create_user(data: dict):
        user = UserModel(**data)
        user.save()
        return user

    @staticmethod
    def find_by_email(email: str):
        return UserModel.objects(email=email).first()
