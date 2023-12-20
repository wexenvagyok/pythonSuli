from tkinter import *
import math

def eltol(pontok,x,y):
    for a in range(0,len(pontok),2):
        pontok[a]+=x
        pontok[a+1]+=y
    return(pontok)

win=Tk()

win.geometry("600x600")

canvas=Canvas(win, width=600, height=300)
canvas.configure(bg="lightgray")
canvas.pack(fill = BOTH, expand = 1)

pontok=[0,0,100,0,100,100,0,100,0,0]

for a in range(0,len(pontok),2):
    pontok[a]+=200
    pontok[a+1]+=100
    
canvas.create_line(pontok, width=2.5,fill="green")
pntok=eltol(pontok,0,100)
canvas.create_line(pontok, width=2.5,fill="green")
win.mainloop()