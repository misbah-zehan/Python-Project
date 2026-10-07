def task():
    tasks=[]
    print("---WELCOME TO THE TASK MANAGEMENT APP---")

    total_task= int(input("Enter the number of tasks you want to add: "))
    for i in range(1,total_task+1):
        task_name=input(f"Enter the name of task {i}: ")
        tasks.append(task_name)
    print(f"Today's tasks are:\n {tasks}")

    while True:
        operatiom = int (input("Enter 1-Add task\n2-Update task\n3-Delete task\n4-View tasks\n5-Exit\nChoose an operation:"))
        if operatiom == 1:
            add=input("Enter the task you want to add: ")
            tasks.append(add)
            print(f"Task '{add}' added successfully.")
        elif operatiom == 2:
            update_index = input("Enter the name of the task you want to update: ")
            if update_index in tasks:
                new_task = input("Enter the new task: ")
                ind = tasks.index(update_index)
                tasks[ind] = new_task
                print(f"Task at index {update_index} updated successfully.")
        elif operatiom == 3:
            delete_index = input("Enter the name of the task you want to delete: ")
            if delete_index in tasks:
                ind = tasks.index(delete_index)
                del tasks[ind]
                print(f"Task '{delete_index}' deleted successfully.")
        elif operatiom == 4:
            print(f"Today's tasks are:\n {tasks}")
        elif operatiom == 5:
            print("Exiting the task management app. Goodbye!")
            break
        else:
            print("Invalid operation. Please try again.")
task()
                