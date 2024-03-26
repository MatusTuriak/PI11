# NAHODNE STVORCE
# import turtle,random
#
# def stvorec(dlzka):
#     for i in range(4):
#         t.fd(dlzka)
#         t.rt(90)
#
# def posun():
#     t.pu()
#     t.setpos(random.randint(-100,100), random.randint(-100,100))
#     t.seth(random.randint(0,359))
#     t.pd()
#
#
# t = turtle.Turtle()
# turtle.delay(0)
# for i in range(10):
#     posun()
#     stvorec(30)
# turtle.done()

#DOMCEKY
# import turtle,random
#
# def stvorec(dlzka):
#     for i in range(4):
#         t.fd(dlzka)
#         t.rt(90)
#
# def trojuholnik(dlzka):
#     for i in range(3):
#         t.fd(dlzka)
#         t.rt(120)
#
# def dom(d):
#     t.pencolor("blue")
#     stvorec(d)
#     t.lt(60)
#     t.pencolor("red")
#     trojuholnik(d)
#     t.rt(60)
#
# def posun():
#     t.pu()
#     t.setpos(random.randint(-150,150),random.randint(-100,100))
#     t.seth(random.randint(-30,30))
#     t.pd()
#
# turtle.delay(0)
# t = turtle.Turtle()
# t.pensize(5)
# for i in range(20):
#     posun()
#     dom(30)
# turtle.done()

# t.fillcolor(f'#{random.randrange(256 ** 3):06x}')

#NUHLONIK
# import turtle
#
# def n_uholnik(n, d):
#     for i in range(n):
#         t.fd(d)
#         t.lt(360/n)
#
# turtle.delay(0)
# t = turtle.Turtle()
# for n in range(3,16):
#     n_uholnik(n,50)
# turtle.done()

#KVET
# import turtle
#
# def obluk(d):
#     for i in range(9):
#         t.fd(d)
#         t.rt(10)
#
# def lupen(d):
#     for i in 1, 2:
#         obluk(d)
#         t.rt(90)
#
# def kvet(n, d):
#     for i in range(n):
#         lupen(d)
#         t.rt(360/n)
#
# turtle.delay(0)
# t = turtle.Turtle()
# kvet(20,20)
# turtle.done()

#SPIRALY
# import turtle
#
# turtle.delay(0)
# t = turtle.Turtle()
# for uhol in range(1, 2000):
#     t.fd(8)
#     t.rt(uhol + 0.1)
# turtle.done()

# KRUHY
# import tkinter
#
# def klik(event):
#     x, y = event.x, event.y
#     canvas.create_oval(x-10, y-10, x+10, y+10, fill='red')
#
# canvas = tkinter.Canvas()
# canvas.pack()
# canvas.bind('<ButtonPress>', klik)
#
# tkinter.mainloop()



