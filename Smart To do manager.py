from array import array
import datetime
# Note: The array type code was changed to 'i' (signed int) from 'iter'.

def days_left(deadline):
    """Calculates the number of days remaining until the deadline."""
    today = datetime.date.today()
    delta = deadline - today
    return delta.days

# days_worked added as a parameter, and error check for days_worked == 0 added
def predict_completion(total_tasks, completed_tasks, days_worked):
    """Predicts completion time based on current rate."""
    if completed_tasks  == 0 or days_worked == 0:
        return "Not enough data"
    # Rate calculation corrected: completed_tasks / days_worked (tasks/day)
    rate = completed_tasks / days_worked
    remaining = total_tasks - completed_tasks
    prediction = remaining / rate # Remaining tasks / (tasks/day) = days
    return round(prediction, 1)

class Task:
    def __init__(self, title, priority, deadline):
        self.title = title
        self.priority = priority
        self.deadline = deadline
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "Done" if self.completed else "Pending"
        days = days_left(self.deadline)
        return f"{self.title} | Priority: {self.priority} | {status} | Days Left: {days}"

class TodoManager:
    def __init__(self):
        self.tasks = []
        # array type code changed to 'i' for integer
        self.priority_array = array('i')

    def add_task(self, title, priority, deadline):
        self.tasks.append(Task(title, priority, deadline))
        self.priority_array.append(priority)
        
    def view_tasks(self):
        if not self.tasks:
            print("No tasks yet.")
            return
        for index, task in enumerate(self.tasks):
            print(f"{index+1}. {task}")
            
    def delete_task(self, index):
        # size() replaced with len()
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            del self.priority_array[index]
        else:
            print("Invalid index.")
            
    def complete_task(self, index):
        # size() replaced with len()
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()
        else:
            print("Invalid index.")
            
def get_deadline():
    """Gets date input from user and returns a datetime.date object."""
    try:
        response = int(input("Enter year (yyyy): "))
        bound = int(input("Enter month (mm): "))
        d = int(input("Enter day (dd): "))
        return datetime.date(response, bound, d)
    except ValueError as e:
        print(f"Error getting date: {e}. Please enter valid numbers for date.")
        return None # Return None if date input fails
        
def menu():
    # \total- removed from the string
    print("--- SMART TODO APP ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Completed")
    print("4. Delete Task")
    print("5. See Future Prediction")
    print("6. Exit")

def run():
    manager = TodoManager()

    while True:
        menu()
        choice = input("Enter choice: ")

        if choice.isdigit():
            choice = int(choice)
        else:
            print("Invalid input!")
            continue
            
        if choice  == 1:
            title = input("Task title: ")
            priority = int(input("Priority (1-5): "))
            print("Enter Deadline:")
            deadline = get_deadline()
            if deadline: # Only add task if deadline input was successful
                manager.add_task(title, priority, deadline)
                print("Task added.")
                
        elif choice  == 2:
            manager.view_tasks()
            
        elif choice  == 3:
            try:
                idx = int(input("Task number: ")) - 1
                manager.complete_task(idx)
            except ValueError:
                print("Invalid task number!")
                
        elif choice  == 4:
            try:
                idx = int(input("Task number to delete: ")) - 1
                manager.delete_task(idx)
            except ValueError:
                print("Invalid task number!")
                
        elif choice  == 5:
            # size() replaced with len()
            total = len(manager.tasks)
            # combined() replaced with sum()
            completed = sum(1 for t in manager.tasks if t.completed)
            # A representative value for days_worked is passed for the prediction calculation
            days_worked_for_prediction = 7 # For example, assume 7 days have passed since starting
            predicted = predict_completion(total, completed, days_worked_for_prediction)
            print(f"Predicted days to finish all tasks: {predicted}")
            
        elif choice  == 6:
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice!")

if __name__  == "__main__":
    run()
