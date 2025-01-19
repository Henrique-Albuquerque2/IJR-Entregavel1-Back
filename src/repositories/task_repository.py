from models.task import TaskModel

class TaskRepository:
    @staticmethod
    def create_task(data: dict):
        task = TaskModel(**data)
        task.save()
        return task

    @staticmethod
    def get_all_tasks_by_user(owner_id: str):
        return TaskModel.objects(owner=owner_id)  # Filtra tarefas pelo dono

    @staticmethod
    def get_task_by_id_and_user(task_id: str, owner_id: str):
        return TaskModel.objects(id=task_id, owner=owner_id).first()

    @staticmethod
    def update_task(task_id: str, data: dict, owner_id: str):
        task = TaskModel.objects(id=task_id, owner=owner_id).first()
        if task:
            task.update(**data)
            return task.reload()
        return None

    @staticmethod
    def delete_task(task_id: str, owner_id: str):
        task = TaskModel.objects(id=task_id, owner=owner_id).first()
        if task:
            task.delete()
            return True
        return False
