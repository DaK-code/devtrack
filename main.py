tasks = []

def add_task(task):
    tasks.append(task)
    print(f"✅ Added : {task}")

def show_tasks():
    print("\n📋 current Tasks : ")
    for i,t in enumerate(tasks, start = 1):
        print(f"{i}. {t}")

if __name__ == "__main__":
    add_task("Setup repository")
    add_task("Write documentation")
    show_tasks()