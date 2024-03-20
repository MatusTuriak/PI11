# import tkinter
# import random
#
# def vypis():
#     text = "PYTHON"
#     x = random.randrange(50,330)
#     y = random.randrange(50,330)
#     canvas.create_text(x , y , text=text, font="arial 20")
#
# def zmaz():
#     canvas.delete("all")
#
# canvas = tkinter.Canvas()
# canvas.pack()
# tkinter.Button(text="Vypis text", command=vypis).pack()
# tkinter.Button(text="zmaz plochu", command=zmaz).pack()
#
# vstup = tkinter.Entry(width=10)
# vstup.pack()
#
# tkinter.mainloop()
import tkinter
# import tkinter
#
# def klik(event):
#     canvas.create_line(100, 200, event.x, event.y)
#     x, y = event.x, event.y
#     canvas.create_oval(x-10, y-10, x+10, y+10, fill='red')

#
# canvas = tkinter.Canvas()
# canvas.pack()
# canvas.bind('<ButtonPress>', klik)
#
# tkinter.mainloop()

# import tkinter
#
# def klik(event):
#     # x, y = event.x, event.y
#     # canvas.create_oval(x-10, y-10, x+10, y+10, fill="red")
#     global xx, yy
#     xx, yy = event.x, event.y
#
# def tahaj(event):
#     # x, y = event.x, event.y
#     # canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill='blue')
#     canvas.create_line(xx, yy, event.x, event.y)
#
# canvas = tkinter.Canvas()
# canvas.pack()
# canvas.bind('<B1-Motion>', tahaj)
# canvas.bind('<ButtonPress>',klik)
#
# tkinter.mainloop()

# import tkinter
# import random
#
# zoznam = []
#
# def klik(event):
#     global poly
#     zoznam[:] = [event.x, event.y]
#     farba = f"#{random.randrange(256**3):06x}"
#     poly = canvas.create_polygon(0,0,0,0,fill=farba)
#     # ciara = canvas.create_line(0, 0, 0, 0)
#
# def tahaj(event):
#     zoznam.extend([event.x, event.y])
#     canvas.coords(poly, zoznam)
#
# canvas = tkinter.Canvas()
# canvas.pack()
# canvas.bind('<ButtonPress>', klik)
# canvas.bind('<B1-Motion>', tahaj)
#
# tkinter.mainloop()

# import tkinter
#
# x, y = 200,200
# zoznam = [x,y]
#
# def kresli(dx, dy):
#     global x, y
#     x += dx
#     y += dy
#     zoznam.extend((x, y))
#     canvas.coords(ciara, zoznam)
#
# def vlavo(event):
#     kresli(-10, 0)
#
# def vpravo(event):
#     kresli(10, 0)
#
# def hore(event):
#     kresli(0, -10)
#
# def dole(event):
#     kresli(0, 10)
#
#
# canvas = tkinter.Canvas()
# canvas.pack()
#
# ciara = canvas.create_line(10,10,-10,-10)
# canvas.bind_all("<Left>", vlavo)
# canvas.bind_all("<Right>", vpravo)
# canvas.bind_all("<Up>" , hore)
# canvas.bind_all("<Down>", dole)
#
# for i in range(10):
#
#
#
#
# tkinter.mainloop()

import turtle

def dopredu():
    t.fd(30)

def vpravo():
    t.rt(90)

def vlavo():
    t.lt(90)

t = turtle.Turtle()
t.pu()
tkinter.Button(text=">", command = dopredu).pack()
tkinter.Button(text="+", command = vpravo).pack()
tkinter.Button(text="-", command = vlavo).pack()


turtle.bgcolor("black")
t.shape("turtle")
t.shapesize(2, 2, 4)
t.color("dark green","green")

turtle.done()