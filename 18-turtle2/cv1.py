#2.
# import turtle,tkinter
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
# tkinter.Button(text="dopredu",command=dopredu).pack(side="left")
# tkinter.Button(text="vpravo",command=vpravo).pack(side="left")
# tkinter.Button(text="vlavo",command=vlavo).pack(side="left")
# tkinter.Button(text="begin_fill",command=begin).pack(side="left")
# tkinter.Button(text="end_fill",command=end).pack(side="left")
#
# t.pensize(3)
# t.color("blue","red")
#
# turtle.done()
#
# import turtle,tkinter,random
#
#3.
# def slnko(pocet,velkost):
#     t.pencolor("gold")
#     t.pensize(10)
#     for i in range(pocet):
#         t.fd(velkost)
#         t.fd(-velkost)
#         t.rt(360/pocet)
#     t.dot(velkost)
#
# def nove_slnko():
#     t.clear()
#     slnko(random.randint(3,20),random.randint(20,100))
#
# turtle.delay(0)
# t = turtle.Turtle()
# tkinter.Button(text="nove slnko",command=nove_slnko).pack()
# t.speed(0)
# slnko(12,100)
#
# turtle.done()
#
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
#
# terc(20)
#
# turtle.done()
#7.
# import turtle
#
# def kosostvorec(velkost,farba):
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
#     kosostvorec(100, ("tan","tomato")[i % 2])
#     t.lt(45)
#
# turtle.done()
#
#10
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
#
#11.
#
# import turtle, random
#
# def bodky(n,m):
#     t.pencolor("salmon")
#     t.pu()
#     for i in range(n):
#         for j in range(m):
#             t.dot(random.randint(20, 35))
#             t.fd(30)
#         t.fd(-m * 30)
#         t.lt(90)
#         t.fd(30)
#         t.rt(90)
#
# turtle.delay(0)
# t = turtle.Turtle()
#
# bodky(10,15)
#
# turtle.done()
#
#12.
#
# import turtle
# import random
#
# def stvorec(dlzka):
#     t.fillcolor(f'#{random.randrange(256**3):06x}')
#     t.begin_fill()
#     for i in range(4):
#         t.fd(dlzka)
#         t.rt(90)
#     t.end_fill()
#
# def stvorce(dlzka, krok):
#     t.pu()
#     while dlzka > 0:
#         stvorec(dlzka)
#         t.fd(krok / 2)
#         t.rt(90)
#         t.fd(krok / 2)
#         t.lt(90)
#         dlzka -= krok
#
# turtle.delay(0)
# t = turtle.Turtle()
#
# stvorce(200, 25)
#
# turtle.done()
#
#13.

# import turtle
# import random
#
# def stvorec(dlzka):
#     t.fillcolor(f'#{random.randrange(256**3):06x}')
#     t.begin_fill()
#     for i in range(4):
#         t.fd(dlzka)
#         t.rt(90)
#     t.end_fill()
#
# def veza(dlzka, krok):
#     t.pu()
#     while dlzka > 0:
#         stvorec(dlzka)
#         dlzka -= krok
#         t.fd(krok / 2)
#         t.lt(90)
#         t.fd(dlzka)
#         t.rt(90)
#
# turtle.delay(0)
# t = turtle.Turtle()
#
# veza(120, 30)
#
# turtle.done()