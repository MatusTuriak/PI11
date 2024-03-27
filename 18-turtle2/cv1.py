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
# import turtle
#
# def kosostvorec(velkost,farba):
#     t.fillcolor(farba)
#     t.begin_fill()
#     for i in range(8):
#         t.fd(velkost)
#         t.rt(45)
#         t.fd(velkost)
#         t.rt(135)
#     t.end_fill()
#
# turtle.delay(0)
# t = turtle.Turtle()
# for i in range(8):
#     kosostvorec(100,("tan","tomato")[i % 2])
#     t.lt(45)
#
# turtle.done()