import tkinter as tk 
from tk import *
from PIL import Image, ImageTk

window=tk.Tk()
window.geometry('452x500')
window.title('Ur Pomodoro timer⋆｡˚')
window.config(bg='#9d2c1b')
img = Image.open("C:/Users/Hp/Downloads/pomo.jpeg")
icon = ImageTk.PhotoImage(img)
window.iconphoto(False, icon)

timer=tk.Listbox(window,height=3,width=50,font=('times',15,'bold'))
timer.pack(anchor='center',pady=50,padx=50)

time_left=0
running=False

def set(minutes):
    global time_left ,running
    time_left=minutes*60
    running=False
    txt=f'{minutes:02}'
    timer.delete(0,tk.END)
    timer.insert(tk.END,f'{txt}:00')

def pomo():
    set(25)

def long():
    set(15)

def short():
    set(5)

def countdown():
    global running,time_left
    if running and time_left>0:
        minutes=time_left//60
        seconds=time_left%60
        timer.delete(0,tk.END)
        timer.insert(tk.END,f'{minutes:02}:{seconds:02}')
        time_left-=1
        window.after(1000,countdown)

def start():
    global running
    running=True
    countdown()

def pause():
    global running
    running=False
      
pomodoro=tk.Button(window,text='pomodoro',height=1,width=12,bg='#345a30',activebackground='#345a30',font=('times',15,'bold'),fg='black',command=pomo)
pomodoro.place(x=0)
short_break=tk.Button(window,text='short break',height=1,width=12,bg='#345a30',activebackground='#345a30',font=('times',15,'bold'),fg='black',command=short)
short_break.place(x=154)
long_break=tk.Button(window,text='long break',height=1,width=12,bg='#345a30',activebackground='#345a30',font=('times',15,'bold'),fg='black',command=long)
long_break.place(x=308)
start_btn=tk.Button(window,text='start',height=1,width=12,bg='#345a30',activebackground='#345a30',font=('times',15,'bold'),fg='black',command=start)
start_btn.place(x=60,y=150)
pause_btn=tk.Button(window,text='pause',height=1,width=12,bg='#345a30',activebackground='#345a30',font=('times',15,'bold'),fg='black',command=pause)
pause_btn.place(x=210,y=150)

window.mainloop()
