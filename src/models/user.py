# src/models/user.py
from mongoengine import Document, StringField

class UserModel(Document):
    username = StringField(required=True, unique=True)
    email = StringField(required=True, unique=True)
    password = StringField(required=True)
