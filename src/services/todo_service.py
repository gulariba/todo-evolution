from models.todo_list import TodoList

class TodoService:
    def __init__(self, todo_list=None):
        self.todo_list = todo_list or TodoList()

    def add_task(self, description):
        return self.todo_list.add_task(description)

    def get_tasks(self):
        return self.todo_list.get_tasks()

    def update_task(self, task_id, new_description):
        for task in self.todo_list.get_tasks():
            if task.id == task_id:
                task.description = new_description
                return task
        return None

    def delete_task(self, task_id):
        for task in self.todo_list.get_tasks():
            if task.id == task_id:
                self.todo_list.tasks.remove(task)
                return task
        return None

    def mark_complete(self, task_id):
        for task in self.todo_list.get_tasks():
            if task.id == task_id:
                task.completed = True
                return task
        return None

    def mark_incomplete(self, task_id):
        for task in self.todo_list.get_tasks():
            if task.id == task_id:
                task.completed = False
                return task
        return None

