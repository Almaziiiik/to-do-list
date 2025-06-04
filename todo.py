import json
import os

TODO_FILE = "todo.json"

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def show_tasks(tasks):
    if not tasks:
        print("Нет задач.")
    else:
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def main():
    tasks = load_tasks()
    while True:
        print("\n1. Показать задачи\n2. Добавить задачу\n3. Удалить задачу\n4. Выход")
        choice = input("Выберите действие: ")
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            task = input("Введите новую задачу: ")
            tasks.append(task)
            save_tasks(tasks)
            print("Задача добавлена.")
        elif choice == "3":
            show_tasks(tasks)
            num = input("Введите номер задачи для удаления: ")
            if num.isdigit() and 1 <= int(num) <= len(tasks):
                removed = tasks.pop(int(num)-1)
                save_tasks(tasks)
                print(f"Задача '{removed}' удалена.")
            else:
                print("Неверный номер.")
        elif choice == "4":
            print("Выход.")
            break
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()
