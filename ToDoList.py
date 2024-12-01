class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name, task_description):
        task = Task(task_name, task_description)
        self.tasks.append(task)

    def remove_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                self.tasks.remove(task)
                break

    def mark_task_completed(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                break

    def __str__(self):
        return '\n'.join(str(task) for task in self.tasks)

class Task:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.completed = False

    def __str__(self):
        status = "Completed" if self.completed else "Not Completed"
        return f"Task: {self.name}, Description: {self.description}, Status: {status}"
