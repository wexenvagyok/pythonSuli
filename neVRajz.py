import transzformaciok
from tkinter import *

#create an instance of tkinter frame or window 
win=Tk()

#Set the size of the tkinter window
win.geometry("1200x600")

#Create a canvas widget 
canvas = Canvas(win, width=600, height=600)
canvas.configure(bg="lightgray")
canvas.pack(fill=BOTH, expand=1) #teljes ablakot kitölti 

#fenyo2=[200,0,
#        0,100,
#        150,100,
#        0,200,
#        150,200,
#        0,300,
#        150,300,
#        150,400,
#        250,400,
#        250,300,
#        400,300,
#        250,200,
#        400,200,
#        250,100,
#        400,100,
#        200,0]


#fenyo2masolat = transzformaciok.eltol(fenyo2,100,100)
#canvas.create_line(fenyo2masolat,width=30, fill="darkgreen")

nevB=[[0,0,110,0,110,50,160,50,160,120,0,120,0,0],#fenti lyuk
   [27.5,15,82.5,15,82.5,30,27.5,30,27.5,15],#also lyuk
   [27.5,85,120,85,120,100,27.5,100,27.5,85]]

nevA = [560,200,
        610,0,
        670,0,
        720,200,
        690,200,
        670,150,
        610,150,
        590,200,
        560,200
        ]
nevAbelso = [530,100,
             710,190,
             770,190,
             750,190,
             730,190]

hatter= "ffffff"
betuSzinek = ["blue",hatter,"blue"]


Lori2 = [nevB]
#for e in nevO:
#    e = transzformaciok.eltol(e,0,0)
#    e = transzformaciok.nagyit(e,1)
#    e= transzformaciok.forgat(e,45)

#    Lori2.append(e)
#print(Lori2)
#for e in Lori2:
#    canvas.create_line(e,width=5,fill="blue")

Lori2 = transzformaciok.masol(nevB)

Lori2 = transzformaciok.forgat(Lori2,90)
Lori2 = transzformaciok.nagyit(Lori2,1)   
Lori2 = transzformaciok.eltol(Lori2,0,0)

#for e in Lori2: 
#    canvas.create_line(e,width=5,fill="red")


canvas.create_line(nevB,width=5, fill="blue")
canvas.create_line(nevA,width=5, fill="blue")
#canvas.create_line(nevRbelso,width=5, fill="blue")
canvas.create_line(nevAbelso,width=5, fill="blue")
canvas.create_line(nevA,width=5, fill="blue")
canvas.create_line(nevAbelso,width=5, fill="blue")


win.mainloop()

#while True:
#        canvas.delete("all")
#        Lori2 = transzformaciok.forgat(Lori2,0.1)
#        for e enumerate(Lori2):
#                d = canvas.create_polygon(Lori2,fill= 'blue', outline="blue")
#        
#        win.update_idletasks()
#        win.update()
