from mongoengine import Document, StringField, DateTimeField

class TaskModel(Document):
    title = StringField(required=True)
    description = StringField()
    status = StringField(required=True, choices=["pending", "in_progress", "completed"])
    priority = StringField(default="normal", choices=["low", "normal", "high"])
    due_date = DateTimeField()
    owner = StringField(required=True)  # ID do usuário dono da tarefa
