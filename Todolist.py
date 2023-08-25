import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        pass

def edit_task():
    try:
        selected_task_index = listbox.curselection()[0]
        task_to_edit = listbox.get(selected_task_index)
        entry.delete(0, tk.END)
        entry.insert(tk.END, task_to_edit)
        delete_task()
    except IndexError:
        pass
root = tk.Tk()
root.title("To-Do List")
heading = tk.Label(root, text="To-Do List", font=("Helvetica", 16))
heading.pack(pady=10)
entry = tk.Entry(root, width=30)
entry.pack(pady=10)
add_button = tk.Button(root, text="Submit", command=add_task)
add_button.pack()
listbox = tk.Listbox(root, width=40)
listbox.pack()
edit_button = tk.Button(root, text="Edit", command=edit_task, fg="green")
edit_button.pack()
delete_button = tk.Button(root, text="Delete", command=delete_task, fg="red")
delete_button.pack()

root.mainloop()
