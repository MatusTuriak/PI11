import turtle

turtle.delay(0)
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t1.pu()
t1.setpos(-100,0)
t1.pd()

t2.pu()
t2.setpos(100,0)
t2.pd()

t3.pu()
t3.setpos(0,110)
t3.pd()

for j in range(10):
    t1.lt(36)
    t2.lt(36)
    t3.lt(36)
    for i in range(4):
        t1.fd(50)
        t2.fd(50)
        t3.fd(50)
        t1.lt(90)
        t2.lt(90)
        t3.lt(90)

turtle.mainloop()