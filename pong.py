#egyszerű pong játék
#Start: 2024.01.31
#End: 
#Farkas Balázs
#tanár: Papp Péter

from tkinter import *
import random

def randomcolor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return ("#"+hex(r)[-2:]+hex(g)[-2:]+hex(b)[-2:]).replace("x","0")

jatekHatter = "lightgray"
jatekSpeed = 100

def atmenetColor(red,green,blue):
    red+=5
    if red>255:
        red = red-255
        green+=5
    if green>255:
        green = green-255
        blue+=5
    if blue>255:
        blue = blue-255

    return ("#"+hex(red)[-2:]+hex(green)[-2:]+hex(blue)[-2:]).replace("x","0"),red, green, blue

def rajzol():
        labdaPos[0]+= labdaSpeed[0]
        labdaPos[1]+= labdaSpeed[1]

        if labdaPos[0] > win.winfo_width() or labdaPos[0]<0:
            labdaSpeed[0]*=-1
            #labdaColor = randomcolor()
        if labdaPos[1] > win.winfo_height() or labdaPos[1]<0:
            labdaSpeed[1]*=-1
            #labdaColor = randomcolor()

        labdaLista.append(canvas.create_oval(labdaPos[0],labdaPos[1],labdaPos[0]+labdaSize,labdaPos[1]+labdaSize, fill= labdaColor, outline = ""))

        if len(labdaLista) > labdaListaHossz:
            canvas.delete(labdaLista[0])
            labdaLista.pop(0)
            
        win.after(jatekSpeed,rajzol)
    
print(randomcolor())


win = Tk()
win.geometry("600x600+100+20")
win.title("Pong játék")
canvas = Canvas(win, bg=jatekHatter)
canvas.pack(fill=BOTH, expand= 1)



labda = canvas.create_oval(0,0,100,100,fill="red")

labdaSpeed = [10,15.25]
labdaPos = [200,200]
labdaSize = 50
labdaColor = "red"
red, green, blue = 0,0,0
labdaLista = []
labdaListaHossz= 1

win.after(jatekSpeed,rajzol)
win.mainloop()

while True:
    #labdaColor, red, green, blue=atmenetColor(red,green,blue)
    #print(labdaColor)
    rajzol()
    canvas.update()


win.mainloop()