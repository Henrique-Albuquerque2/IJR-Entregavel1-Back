from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Task(BaseModel):
    title: str
    description: Optional[str] = None
    status: str  # "pending", "in_progress", "completed"
    priority: Optional[str] = "normal"  # "low", "normal", "high"
    due_date: Optional[datetime] = None

    class Config:
        orm_mode = True
