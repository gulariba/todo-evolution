from datetime import datetime
from typing import Optional


class Task:
    """Represents a single todo task."""

    def __init__(self, description: str, task_id: Optional[int] = None):
        """
        Initialize a new task.

        Args:
            description: The task description.
            task_id: Optional unique identifier for the task.

        Raises:
            ValueError: If description is empty or invalid.
        """
        if not description or not description.strip():
            raise ValueError("Task description cannot be empty")

        self.id = task_id
        self.description = description.strip()
        self.completed = False
        self.created_at = datetime.now()

    def mark_completed(self) -> None:
        """Mark the task as completed."""
        self.completed = True

    def mark_pending(self) -> None:
        """Mark the task as pending (not completed)."""
        self.completed = False

    def __str__(self) -> str:
        """String representation of the task."""
        status = "[✓]" if self.completed else "[ ]"
        return f"{status} {self.description}"

    def __repr__(self) -> str:
        """Detailed string representation for debugging."""
        return f"Task(id={self.id}, description='{self.description}', completed={self.completed})"