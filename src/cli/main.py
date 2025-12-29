from services.todo_service import TodoService

def main():
    todo_service = TodoService()
    
    while True:
        command = input("Enter command (add/list/update/delete/complete/incomplete/exit): ")

        if command == "exit":
            break

        elif command.startswith("add"):
            try:
                _, description = command.split(" ", 1)
                task = todo_service.add_task(description)
                print(f"Task added: {task.description} (ID: {task.id})")
            except ValueError:
                print("Invalid command format. Use: add <description>")

        elif command.startswith("update"):
            try:
                _, task_id_str, new_description = command.split(" ", 2)
                task_id = int(task_id_str)
                task = todo_service.update_task(task_id, new_description)
                if task:
                    print(f"Task {task.id} updated to: {task.description}")
                else:
                    print(f"No task found with ID {task_id}")
            except ValueError:
                print("Invalid command format. Use: update <id> <new_description>")

        elif command.startswith("delete"):
            try:
                _, task_id_str = command.split(" ", 1)
                task_id = int(task_id_str)
                task = todo_service.delete_task(task_id)
                if task:
                    print(f"Task {task.id} deleted: {task.description}")
                else:
                    print(f"No task found with ID {task_id}")
            except ValueError:
                print("Invalid command format. Use: delete <id>")

        elif command.startswith("complete"):
            try:
                _, task_id_str = command.split(" ", 1)
                task_id = int(task_id_str)
                task = todo_service.mark_complete(task_id)
                if task:
                    print(f"Task {task.id} marked as complete")
                else:
                    print(f"No task found with ID {task_id}")
            except ValueError:
                print("Invalid command format. Use: complete <id>")

        elif command.startswith("incomplete"):
            try:
                _, task_id_str = command.split(" ", 1)
                task_id = int(task_id_str)
                task = todo_service.mark_incomplete(task_id)
                if task:
                    print(f"Task {task.id} marked as incomplete")
                else:
                    print(f"No task found with ID {task_id}")
            except ValueError:
                print("Invalid command format. Use: incomplete <id>")

        elif command == "list":
            tasks = todo_service.get_tasks()
            if not tasks:
                print("No tasks found.")
            for task in tasks:
                status = "Done" if task.completed else "Pending"
                print(f"{task.id}: {task.description} [{status}]")

        else:
            print("Unknown command")

if __name__ == "__main__":
    main()

