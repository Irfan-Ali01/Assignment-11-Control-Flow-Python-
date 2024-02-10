class Task:
    def __init__(self, title, due_date, priority):
        self.title, self.due_date, self.priority = title, due_date, priority

def add_task(todo_list):
    task = Task(input("Title: "), input("Due date (YYYY-MM-DD): "), input("Priority: "))
    todo_list.append(task)
    print(f"Task '{task.title}' added.")

def categorize_tasks(todo_list):
    return [t for t in todo_list if t.priority == "urgent"], \
           [t for t in todo_list if t.priority == "important"], \
           [t for t in todo_list if t.priority == "less important"]

def main():
    todo_list = []

    while True:
        print("\n1. Add Task\n2. Categorize Tasks\n3. Exit")
        choice = input("Select (1/2/3): ")

        if choice == "1": add_task(todo_list)
        elif choice == "2":
            urgent, important, less_important = categorize_tasks(todo_list)
            print(f"Urgent: {len(urgent)}\nImportant: {len(important)}\nLess Important: {len(less_important)}")
        elif choice == "3": print("Exiting. Have a productive day!"); break
        else: print("Invalid choice. Select 1, 2, or 3.")

if __name__ == "__main__": main()
