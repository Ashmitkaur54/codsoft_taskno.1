import tkinter as tk

root = tk.Tk()
root.title("To-Do List App")
root.geometry("350x450")
root.configure(bg="light blue")

tasks = []

def add_task():
    task_text = entry.get()
    if task_text:
        var = tk.BooleanVar()
        cb = tk.Checkbutton(task_frame, text=task_text, variable=var, onvalue=True, offvalue=False,
                            font=("Arial", 12), anchor="w", width=30, padx=5, bg="white", relief="ridge")
        cb.pack(pady=2, fill='x')
        tasks.append((cb, var))
        entry.delete(0, tk.END)

def delete_selected():
    for task, var in tasks[:]:
        if var.get():
            task.destroy()
            tasks.remove((task, var))

def clear_all():
    for task, var in tasks:
        task.destroy()
    tasks.clear()

title = tk.Label(root, text="My To-Do List", font=("Helvetica", 16, "bold"), bg="light blue")
title.pack(pady=10)

entry = tk.Entry(root, width=28, font=("Arial", 12))
entry.pack(pady=10)

btn_frame = tk.Frame(root, bg="light pink")
btn_frame.pack(pady=5)

add_btn = tk.Button(btn_frame, text="Add Task", width=10, command=add_task)
add_btn.grid(row=0, column=0, padx=5)

delete_btn = tk.Button(btn_frame, text="Delete Tick", width=10, command=delete_selected)
delete_btn.grid(row=0, column=1, padx=5)

clear_btn = tk.Button(btn_frame, text="Clear All", width=10, command=clear_all)
clear_btn.grid(row=0, column=2, padx=5)

task_frame = tk.Frame(root, bg="light blue")
task_frame.pack(pady=10, fill='both', expand=True)

root.mainloop()
