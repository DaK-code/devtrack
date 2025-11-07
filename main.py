tasks = []

def add_task(task, priority = "Normal"):
    tasks.append(f"{task} ({priority})")
    print(f"✅ Added : {task} with priority {priority}")

def show_tasks():
    print("\n📋 current Tasks : ")
    for i,t in enumerate(tasks, start = 1):
        print(f"{i}. {t}")

if __name__ == "__main__":
    add_task("Setup repository")
    add_task("Write documentation")
    show_tasks()

def remove_task(index):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"🗑️ Removed : {removed}")
    else:
        print("⚠️ Invalid index")