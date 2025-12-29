from typing import List, Optional
from models.task import Task



class TodoList:
    """Manages a collection of todo tasks."""

    def __init__(self):
        """Initialize an empty todo list."""
        self.tasks: List[Task] = []
        self._next_id = 1

    def add_task(self, description: str) -> Task:
        """
        Add a new task to the list.

        Args:
            description: The task description.

        Returns:
            The newly created Task object.

        Raises:
            ValueError: If description is invalid.
        """
        task = Task(description, self._next_id)
        self.tasks.append(task)
        self._next_id += 1
        return task

    def get_tasks(self, completed: Optional[bool] = None) -> List[Task]:
        """
        Get tasks from the list.

        Args:
            completed: If True, return only completed tasks.
                      If False, return only pending tasks.
                      If None, return all tasks.

        Returns:
            List of Task objects matching the filter.
        """
        if completed is None:
            return self.tasks.copy()
        return [task for task in self.tasks if task.completed == completed]

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Get a task by its ID.

        Args:
            task_id: The unique identifier of the task.

        Returns:
            The Task object if found, None otherwise.
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def complete_task(self, task_id: int) -> bool:
        """
        Mark a task as completed.

        Args:
            task_id: The unique identifier of the task.

        Returns:
            True if the task was found and marked completed, False otherwise.
        """
        task = self.get_task_by_id(task_id)
        if task:
            task.mark_completed()
            return True
        return False

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task from the list.

        Args:
            task_id: The unique identifier of the task.

        Returns:
            True if the task was found and deleted, False otherwise.
        """
        task = self.get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False

    def __len__(self) -> int:
        """Return the number of tasks in the list."""
        return len(self.tasks)