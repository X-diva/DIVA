import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

window=tk.Tk()
window.title('To do list')
img = Image.open("C:/Users/Hp/Downloads/note.jpeg")
icon = ImageTk.PhotoImage(img)
window.iconphoto(False, icon)

task_frame = Frame(window)
task_frame.grid(row=1, column=0, columnspan=2, sticky="nsew", pady=10)

def add_task():
    the_task = task.get().strip()
    if the_task:  
        single_task_frame = Frame(task_frame)
        single_task_frame.pack(anchor="w", pady=5)
        x = IntVar()
        check = Checkbutton(single_task_frame, variable=x)
        check.pack(side=LEFT)
        task_label = Label(single_task_frame, text=the_task, font=('helvetica', 10))
        task_label.pack(side=LEFT)
        task.delete(0, tk.END)

intro = tk.Label(window, text='*Add your task here:', font=('helvetica', 10, 'bold'), fg='black')
intro.grid(row=0, column=0, padx=10, pady=10, sticky="w")
task = tk.Entry(window, width=35)
task.grid(row=0, column=1, padx=10, pady=5, sticky="w")
add = tk.Button(window, text='add',font=('helvetica', 9, 'bold'), fg='#fbfae4', background='#9f85af', command=add_task, width=10, activebackground='#9f85af')
add.grid(row=0, column=2, padx=10, pady=5, sticky="w")

window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(0, weight=1)

window.mainloop()
