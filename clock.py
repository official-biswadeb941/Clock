#a simple digital clock
from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("A Digital Clock Coded by Biswadeb Mukherjee")
root.resizable(0,0)

def time():
    string = strftime('%H:%M:%S %p %a')
    label.config(text=string)
    label.after(100, time)



label = Label(root, font=("ds-digital", 80,"bold","italic"), background = "black", foreground = "cyan")
label.grid(row=0,column=1)
label.pack(anchor='center')
time()
print("done")

mainloop()