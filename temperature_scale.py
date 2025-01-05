import tkinter as tk
from tkinter import *

window=Tk()

coldimage=PhotoImage(file=r'C:\Users\Hp\Desktop\programmin\hot-sale.png')
cold_image_small = coldimage.subsample(10,10)
coldlabel=Label(window,image=cold_image_small)
coldlabel.pack()

scale=Scale(window,to=-10,from_=40,
            length=400,
            orient=VERTICAL,
            font=('helvetica',15),
            tickinterval=5,
            troughcolor='#9f85af'
            )
scale.pack()

hotimage=PhotoImage(file=r'C:\Users\Hp\Desktop\programmin\snowflake.png')
hot_image_small = hotimage.subsample(10,10) 
hotlabel=Label(window,image=hot_image_small)
hotlabel.pack()

window.mainloop()
