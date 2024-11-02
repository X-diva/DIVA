import tkinter as tk
from tkinter import *
import random

window= tk.Tk()
window.geometry('300x300')
window.title('Tic-Tac-Toe')

def check():
    for row in range(3):
        if buttons[row][0]['text']==buttons[row][1]['text']==buttons[row][2]['text']!='':
          buttons[row][0].config(bg='green')
          buttons[row][1].config(bg='green')
          buttons[row][2].config(bg='green')
          return True
    for column in range(3):
        if buttons[0][column]['text']==buttons[1][column]['text']==buttons[2][column]['text']!='':
           buttons[0][column].config(bg='green')
           buttons[1][column].config(bg='green')
           buttons[2][column].config(bg='green')
           return True
    if buttons[0][0]['text']==buttons[1][1]['text']==buttons[2][2]['text']!='':
       buttons[0][0].config(bg='green')
       buttons[1][1].config(bg='green')
       buttons[2][2].config(bg='green')
       return True
    elif buttons[0][2]['text']==buttons[1][1]['text']==buttons[2][0]['text']!='':
       buttons[0][2].config(bg='green')
       buttons[1][1].config(bg='green')
       buttons[2][0].config(bg='green')
       return True
    elif empty() is False:
        return 'Tie!'
    else: return False
       


def restart_game():
    pass
def next(row,column):
    global player
    if buttons[row][column]['text']=='' and check() is False:
        if player==players[0]:
            buttons[row][column]['text']= player
        if check() is True:
            turn.config(text=players[0] +' is the winner')
        elif check() is False:
            player=players[1]
            turn.config(text=players[1]+' turn')
            buttons[row][column]['text']= player
        elif check()== 'Tie':
            turn.config(text='Tie!')
        else:
            buttons[row][column]['text']= player
        if check() is True:
            turn.config(text=player +' is the winner')
        elif check() is False:
            player=players[0]
            turn.config(text=player+' turn')
            buttons[row][column]['text']= player
        elif check()== 'Tie':
            turn.config(text='Tie!')

def empty():
    spaces=9
    for row in range(3):
        for column in range(3):
            buttons[row][column]['text']!=''
            spaces -=1
        if spaces==0:
            return False
        else:
            return True
players=['X','O']
player=random.choice(players)
turn=tk.Label(window,text=player+' turn',font=('verdana',10))
turn.pack(side='top',ipady=3,pady=3)
rest=tk.Button(window,text='restart',font=('verdana',10),command=restart_game)
rest.pack(side='top',ipady=3,pady=5)
buttons=[[0,0,0],
         [0,0,0],
         [0,0,0]]
frame=tk.Frame(window)
frame.pack()
for row in range(3):
    for column in range(3):
        buttons[row][column]=tk.Button(frame,text='',font=('verdana',10),width=7,height=3,command=lambda row=row,column=column:next(row,column))
        buttons[row][column].grid(row=row,column=column,ipady=3)







window.mainloop()
