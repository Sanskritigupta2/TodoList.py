import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cute To-Do List")
        self.tasks = []
        
        self.root.configure(background="#FFB6C1")  # Set background color to baby pink
        
        self.task_entry = tk.Entry(root, font=("Helvetica", 16))
        self.task_entry.pack(pady=10)
        
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task, font=("Helvetica", 12))
        self.add_button.pack(pady=5)
        
        self.task_list = tk.Listbox(root, height=10, width=50, font=("Helvetica", 12))
        self.task_list.pack()
        
        self.complete_button = tk.Button(root, text="Complete Task", command=self.complete_task, font=("Helvetica", 12))
        self.complete_button.pack(pady=5)
        
        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task, font=("Helvetica", 12))
        self.remove_button.pack(pady=5)
        
        self.refresh_list()
        
    def refresh_list(self):
        self.task_list.delete(0, tk.END)
        for task in self.tasks:
            self.task_list.insert(tk.END, task)
    
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_entry.delete(0, tk.END)
            self.refresh_list()
        else:
            messagebox.showwarning("Warning", "Please enter a task.")
        
    def complete_task(self):
        selected_task = self.task_list.curselection()
        if selected_task:
            index = selected_task[0]
            self.tasks[index] = "✓ " + self.tasks[index]
            self.refresh_list()
        
    def remove_task(self):
        selected_task = self.task_list.curselection()
        if selected_task:
            index = selected_task[0]
            del self.tasks[index]
            self.refresh_list()

root = tk.Tk()
app = TodoApp(root)
root.mainloop()
