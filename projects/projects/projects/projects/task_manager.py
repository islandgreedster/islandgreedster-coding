"""
Task Manager
------------
A simple command-line style task manager program.
Created by islandgreedster 🚀
"""

import datetime

class Task:
    def __init__(self, title, priority="Medium"):
        self.title = title
        self.priority = priority
        self.created_at = datetime.datetime.now()
        self.completed = False

    def mark_done(self):
        self.completed = True

    def __repr__(self):
        status = "✅ Done" if self.completed else "❌ Not done"
        return f"[{self.priority}] {self.title} - {status} (Created: {self.created_at:%Y-%m-%d %H:%M})"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, priority="Medium"):
        task = Task(title, priority)
        self.tasks.append(task)

    def show_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_done()
        else:
            print("Invalid task number.")


# Demo usage
if __name__ == "__main__":
    manager = TaskManager()
    manager.add_task("Finish GitHub repo setup", "High")
    manager.add_task("Practice Python coding", "Medium")
    manager.add_task("Plan future projects", "Low")

    print("\n📋 Task List:")
    manager.show_tasks()

    print("\nMarking first task as done...\n")
    manager.complete_task(0)
    manager.show_tasks()
  
