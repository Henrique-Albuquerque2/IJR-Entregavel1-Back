from mongoengine import Document, StringField, DateTimeField

class TaskModel(Document):
    title = StringField(required=True)
    description = StringField()
    status = StringField(required=True, choices=["pendente", "emProgresso", "finalizada"])
    priority = StringField(default="média", choices=["baixa", "média", "alta"])
    due_date = DateTimeField()
    owner = StringField(required=True)  # ID do usuário dono da tarefa
