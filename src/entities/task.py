# src/entities/task.py
from pydantic import BaseModel
from typing import Optional
import dotenv
dotenv.load_dotenv()

class Task(BaseModel):
    title: str
    description: Optional[str]
    status: str = "Pendente"  # Padrão: Pendente
    priority: str = "Média"  # Padrão: Média
    due_date: Optional[str]
