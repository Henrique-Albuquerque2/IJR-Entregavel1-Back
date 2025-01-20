from mongoengine import Document, StringField, DateTimeField

class TaskModel(Document):
    title = StringField(required=True)
    description = StringField()
    status = StringField(required=True, choices=["pendente", "emProgresso", "finalizada"])
    priority = StringField(default="média", choices=["baixa", "média", "alta"])
    due_date = DateTimeField()
    owner = StringField(required=True)  # ID do usuário dono da tarefa

    def to_json(self):
        """Sobrescreve o método para converter o _id em string."""
        task = super().to_mongo().to_dict()
        task["_id"] = str(self.id)  # Converte ObjectId para string
        return task
