import turtle
import random


t = turtle.Turtle()
turtle.delay(0)

def obluk(d):
    for i in range(9):
        t.fd(d)
        t.lt(10)

def lupen(d):
    for i in range(2):
        obluk(d)
        t.lt(90)

def kvet(n, d):
    for j in range(4):
        for i in range(n):
            t.fillcolor(random.choice(("red", "blue","green","yellow","purple","orange","pink")))
            t.begin_fill()
            lupen(d)
            t.end_fill()
            t.lt(360 / n)
        t.pu()
        t.fd(200)
        t.lt(90)
        t.pd()



kvet(20, 10)

turtle.mainloop()