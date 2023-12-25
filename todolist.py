from tkinter import *
from tkinter import messagebox

def newTask():
    task = my_entry.get()
    if task.strip() != "":
        lb.insert(END, task)
        my_entry.delete(0, END)
    else:
        messagebox.showinfo("Note", "Please enter some task.")

def deleteTask():
    selected_task = lb.curselection()
    if selected_task:
        lb.delete(selected_task)
    else:
        messagebox.showinfo("Note", "Please select a task to delete.")

# Creating the main window
workspace = Tk()
workspace.geometry('500x400+500+200')
workspace.title('TO_DO LIST')
workspace.config(bg='#223441')
workspace.resizable(width=False, height=False)

# Create widgets (frame, listbox, scrollbar, entry, buttons)
frame = Frame(workspace)
frame.pack(pady=10)

lb = Listbox(
    frame,
    width=25,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
)
lb.pack(side=LEFT, fill=BOTH)

task_list = [
    'Study French vocabulary',
    'Online maths lesson',
    'Study flashcard sets',
    'Finish portfolio work for visual arts',
    'Attend guitar classes'
]

for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)
lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
    workspace,
    font=('Times', 24)
)
my_entry.pack(pady=20)

button_frame = Frame(workspace)
button_frame.pack(pady=20)

addTask_btn = Button(
    button_frame,
    text='Add Task',
    font=('Times', 14),
    bg='#c5f776',
    padx=20,
    pady=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=TRUE, side=LEFT)

delTask_btn = Button(
    button_frame,
    text='Delete Task',
    font=('Times', 14),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=TRUE, side=LEFT)

# Creating mainloop
workspace.mainloop()
