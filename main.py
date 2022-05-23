asks = [
    {'name' : 'Write email to Jan', 'completed' : 'True'},
    {'name' : 'Sweep front porch', 'completed' : 'False'},
    {'name' : 'Call mom', 'completed' : 'False'}
]
def list_tasks():
    for index, task in enumerate(tasks):
        print(str.format('{}: {} (Completed: {})', index, task['name'], task['completed']))
def add_task():
    task_text = input('Please add a task: ')
    add_task = {'name': task_text, 'completed' : 'False'}
    tasks.append(add_task)
    print()
    print("Task added successfully!")
program_is_running = True
while program_is_running:
    menu_text = """
====================
1. List the tasks
2. Add a task
3. Remove a task
4. Mark task complete
5. Quit

What would you like to do? """
    try:
        decision =int(input(menu_text))
    except:
        print("Invalid Input! Please try again!\n")
        continue
    if decision == 1:
        list_tasks()
    elif decision == 2:
        add_task()
    elif decision == 3:
        list_tasks()
        index = int(input('Please choose index number of the task to be removed: '))
        try:
            del tasks[index]
            print()
            print('Task removed successfully!')
        except:
            print()
            print('Wrong task index number..Restart from beginning.')
            continue
    elif decision == 4:
        list_tasks()
        index1 = int(input('Please choose index number of the task to be marked: '))
        try:
            tasks[index1]['completed'] = 'True'
            print()
            print('Task marked successfully!')
        except:
            print()
            print('Wrong task index number..Restart from beginning.')
            continue
    elif decision == 5:
        program_is_running = False
    else:
        print('please choose a valid option')