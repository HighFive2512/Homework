from project.task import Task
from typing import List


class Section:

    def __init__(self, name: str):
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        try:
            task = next(filter(lambda t: t.name == task_name, self.tasks))
        except StopIteration:
            return f"Could not find task with the name {task_name}"

        task.completed = True
        return f"Completed task {task_name}"

    def clean_section(self):
        c_task = 0
        for eachtask in self.tasks:
            if eachtask.completed:
                self.tasks.remove(eachtask)
                c_task += 1
        return f"Cleared {c_task} tasks."

    def view_section(self):
        tasks_with_details = "\n".join(t.details() for t in self.tasks)
        return f"Section {self.name}:\n{tasks_with_details}"
