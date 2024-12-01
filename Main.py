
# Main application class for the To-Do list GUI

import tkinter as tk
from tkinter import messagebox
from ToDoList import ToDoList

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        
        # Set window size and center it on the screen
        window_width = 400
        window_height = 400
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calculate the position to center the window
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)

        # Set the position of the window
        self.root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
        
        self.todo_list = ToDoList()

        # Create the title label
        self.title_label = tk.Label(self.root, text="To-Do List", font=("Arial", 24))
        self.title_label.pack(pady=10)

        # Create input field for task name
        self.task_name_label = tk.Label(self.root, text="Task Name:")
        self.task_name_label.pack(pady=5)
        self.task_name_entry = tk.Entry(self.root)
        self.task_name_entry.pack(pady=5)

        # Create input field for task description
        self.task_description_label = tk.Label(self.root, text="Task Description:")
        self.task_description_label.pack(pady=5)
        self.task_description_entry = tk.Entry(self.root)
        self.task_description_entry.pack(pady=5)

        # Button to add a task
        self.add_task_button = tk.Button(self.root, text="Add Task", command=self.add_task, font=("Arial", 12))
        self.add_task_button.pack(pady=10)

        # Button to show all tasks
        self.show_tasks_button = tk.Button(self.root, text="Show All Tasks", command=self.show_tasks, font=("Arial", 12))
        self.show_tasks_button.pack(pady=10)

        # Button to mark a task as completed
        self.mark_completed_button = tk.Button(self.root, text="Mark Task as Completed", command=self.mark_completed, font=("Arial", 12))
        self.mark_completed_button.pack(pady=10)

        # Button to remove a task
        self.remove_task_button = tk.Button(self.root, text="Remove Task", command=self.remove_task, font=("Arial", 12))
        self.remove_task_button.pack(pady=10)

        # Textbox to display the list of tasks
        self.task_display = tk.Text(self.root, height=10, width=50)
        self.task_display.pack(pady=10)

    # Function to add a new task
    def add_task(self):
        task_name = self.task_name_entry.get()
        task_description = self.task_description_entry.get()

        if task_name and task_description:
            self.todo_list.add_task(task_name, task_description)
            self.task_name_entry.delete(0, tk.END)
            self.task_description_entry.delete(0, tk.END)
            messagebox.showinfo("Task Added", f"Task '{task_name}' added successfully!")
        else:
            messagebox.showwarning("Input Error", "Please provide both task name and description.")

    # Function to display all tasks
    def show_tasks(self):
        self.task_display.delete(1.0, tk.END)
        if self.todo_list.tasks:
            for task in self.todo_list.tasks:
                self.task_display.insert(tk.END, f"{task}\n")
        else:
            self.task_display.insert(tk.END, "No tasks available.")

    # Function to mark a task as completed
    def mark_completed(self):
        task_name = self.task_name_entry.get()

        if task_name:
            self.todo_list.mark_task_completed(task_name)
            messagebox.showinfo("Task Completed", f"Task '{task_name}' marked as completed!")
            self.show_tasks()  # Update the task list display
        else:
            messagebox.showwarning("Input Error", "Please enter a task name to mark as completed.")

    # Function to remove a task
    def remove_task(self):
        task_name = self.task_name_entry.get()

        if task_name:
            self.todo_list.remove_task(task_name)
            messagebox.showinfo("Task Removed", f"Task '{task_name}' removed successfully!")
            self.show_tasks()  # Update the task list display
        else:
            messagebox.showwarning("Input Error", "Please enter a task name to remove.")

# Main function to run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
