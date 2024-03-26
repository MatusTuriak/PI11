#1.
# import turtle
# import tkinter
#
# def dopredu():
#     t.fd(50)
#
# def vpravo():
#     t.rt(90)
#
# def vlavo():
#     t.lt(18)
#
# t = turtle.Turtle()
# tkinter.Button(text='Dopredu', command=dopredu).pack(side='left')
# tkinter.Button(text='Vpravo', command=vpravo).pack(side='left')
# tkinter.Button(text='Vlavo', command=vlavo).pack(side='left')
#
# t.pensize(3)
# t.color('blue', 'red')
#
# turtle.done()
#2.
# import turtle
# import tkinter
#
# def dopredu():
#     t.fd(50)
#
# def vpravo():
#     t.rt(90)
#
# def vlavo():
#     t.lt(18)
#
# def begin():
#     t.begin_fill()
#
# def end():
#     t.end_fill()
#
# t = turtle.Turtle()
# tkinter.Button(text='Dopredu', command=dopredu).pack(side='left')
# tkinter.Button(text='Vpravo', command=vpravo).pack(side='left')
# tkinter.Button(text='Vlavo', command=vlavo).pack(side='left')
# tkinter.Button(text='begin_fill', command=begin).pack(side='left')
# tkinter.Button(text='end_fill', command=end).pack(side='left')
#
# t.pensize(3)
# t.color('blue', 'red')
#
# turtle.done()
# #3.
# import turtle
# import tkinter
# import random
#
# def slnko(pocet, velkost):
#     t.pencolor('gold')
#     t.pensize(10)
#     for i in range(pocet):
#         t.fd(velkost)
#         t.fd(-velkost)
#         t.rt(360 / pocet)
#     t.dot(velkost)
#
# def nove_slnko():
#     t.clear()
#     slnko(random.randint(3, 20), random.randint(20, 100))
#
# turtle.delay(0)
# t = turtle.Turtle()
# tkinter.Button(text='Nové slnko', command=nove_slnko).pack()
# t.speed(0)
# slnko(12, 100)
#
# turtle.done()
#4.
# import turtle
# import tkinter
#
# def terc(n, farba1='blue', farba2='yellow'):
#     for i in reversed(range(1, n + 1)):
#         t.dot(i * 15, farba1)
#         farba1, farba2 = farba2, farba1
#
# def prekresli():
#     t.clear()
#     terc(20, farba1.get(), farba2.get())
#
# turtle.delay(0)
# t = turtle.Turtle()
# farba1 = tkinter.Entry()
# farba1.pack()
# farba2 = tkinter.Entry()
# farba2.pack()
# tkinter.Button(text='Prekresli', command=prekresli).pack()
#
# terc(20)
#
# turtle.done()

#5.
# import turtle
# import random
# import tkinter
#
# def strom(kmen, koruna):
#     t.lt(90)
#     t.pensize(15)
#     t.pencolor('brown')
#     t.fd(kmen)
#     t.pensize(40)
#     t.pencolor('green')
#     t.fd(koruna)
#     t.pu()
#     t.bk(kmen+koruna)
#     t.pd()
#     t.rt(90)
#
# def pridaj():
#     strom(random.randint(30, 60), random.randint(10, 40))
#     t.pu()
#     t.fd(50)
#     t.pd()
#
# def uber():
#     t.pu()
#     t.fd(-50)
#     t.pd()
#     t.lt(90)
#     t.pencolor('white')
#     t.pensize(40)
#     t.fd(100)
#     t.fd(-100)
#     t.rt(90)
#
# turtle.delay(0)
# t = turtle.Turtle()
# tkinter.Button(text='Pridaj', command=pridaj).pack()
# tkinter.Button(text='Uber', command=uber).pack()
# t.speed(0)
# t.pu()
# t.setpos(-250, 0)
# t.pd()
# for i in range(8):
#     pridaj()
#
# turtle.done()
#6.
# import turtle
# import tkinter
#
# def spirala(d, krok, uhol):
#     t.reset()
#     t.speed(0)
#     t.ht()
#     for i in range(200):
#         t.fd(d)
#         t.rt(uhol)
#         d += krok
#         if t.distance(0, 0) > 250:
#             return
#
# def rob(uhol):
#     spirala(5, 3, int(uhol))
#
# turtle.delay(0)
# t = turtle.Turtle()
# tkinter.Scale(command=rob, orient='horizontal', from_=5, to=179, length=300).pack()
#
# spirala(5, 3, 5)
#
# turtle.done()
#7,
# import turtle
#
# def kosostvorec(velkost, farba):
#     t.fillcolor(farba)
#     t.begin_fill()
#     for i in range(2):
#         t.fd(velkost)
#         t.rt(45)
#         t.fd(velkost)
#         t.rt(135)
#     t.end_fill()
#
# turtle.delay(0)
# t = turtle.Turtle()
# for i in range(8):
#     kosostvorec(100, ('tan', 'tomato')[i % 2])
#     t.lt(45)
#
# turtle.done()
#8.
# import turtle
#
# def domcek(d):
#     for i in range(4):
#         t.fd(d)
#         t.lt(90)
#     t.lt(45)
#     d2 = d * 2 ** 0.5
#     t.fd(d2)
#     t.lt(90)
#     t.fd(d2/2)
#     t.lt(90)
#     t.fd(d2/2)
#     t.lt(90)
#     t.fd(d2)
#     t.lt(45)
#
# turtle.delay(0)
# t = turtle.Turtle()
#
# t.rt(5)
# domcek(100)
# domcek(50)
# domcek(80)
#
# turtle.done()

#9.
# import turtle
#
# def polkruznica(velkost, smer):
#     if smer:
#         uhol = 10
#     else:
#         uhol = -10
#     for i in range(18):
#         t.fd(velkost)
#         t.lt(uhol)
#
# turtle.delay(0)
# t = turtle.Turtle()
#
# t.lt(90)
# for i in range(10):
#     polkruznica(3, i % 2)
#
# turtle.done()

#10.
# import turtle
# import random
#
# def polkruh(velkost, smer):
#     if smer:
#         uhol = 10
#     else:
#         uhol = -10
#     t.fillcolor(f'#{random.randrange(256**3):06x}')
#     t.begin_fill()
#     for i in range(18):
#         t.fd(velkost)
#         t.lt(uhol)
#     t.end_fill()
#
# turtle.delay(0)
# t = turtle.Turtle()
#
# t.lt(90)
# for i in range(10):
#     polkruh(3, i % 2)
# for i in range(10):
#     polkruh(3, i % 2 == 0)
#
# turtle.done()