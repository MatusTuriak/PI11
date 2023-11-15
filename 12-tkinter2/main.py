#import tkinter
#import random
#
#canvas = tkinter.Canvas(width=600, height=500)
#canvas.pack()
#x = 3
#xx = x
#y = 10
#d = 30
#pocet = 598 // d  # //je celociselne delenie 7 // 3 = 2
#for j in range(498 // d):
#    for i in range(pocet):
#        farba = random.choice(("green","purple","red"))
#        canvas.create_rectangle(x ,y ,x+d ,y+d ,fill=farba)
#        canvas.create_line(x ,y ,x+d ,y+d)#ciara
#        canvas.create_line(x ,y+d ,x+d ,y)
#        x = x + d
#    y = y + d
#    x = xx
#
#
#
#canvas.mainloop()
import tkinter
import random

canvas=tkinter.Canvas(width=600, height=500)
canvas.pack()
x = 3
xx = x
y = 10
d = 30
stvrtina = d//4
pocet = 598 // d  # //je celociselne delenie 7 // 3 = 2
for j in range(498 // d):
    for i in range(pocet):
        canvas.create_rectangle(x ,y+d//2 ,x+d ,y+d//2+d ,)
        canvas.create_line(x+d//2 ,y ,x ,y+d//2)
        canvas.create_line(x+d//2 ,y ,x+d ,y+d//2)
        canvas.create_rectangle(x+stvrtina,y+3*stvrtina ,x+3*stvrtina, y + d + stvrtina)
        canvas.create_line
        x = x + d
    y = y + d + d // 2
    x = xx


canvas.mainloop()
#canvas.create_polygon(10, 10, 100, 10, 100, 100, fill="red")