import tkinter

canvas = tkinter.Canvas(width=600, height=500)
canvas.pack()
x = 20
xx = x
y = 30
d = 3
f = "black"
dlzkaslova = 30 * d
vyskaslova = 7 * d
pocet = 598 // dlzkaslova
for j in range(498 // vyskaslova):
    for i in range(pocet):
        canvas.create_rectangle(x, y, x+d, y+d ,)
        canvas.create_rectangle(x+d, y+d, x+2*d, y+2*d ,fill = f)
        canvas.create_rectangle(x+2*d, y+2*d, x+3*d, y+3*d ,fill = f)
        canvas.create_rectangle(x ,y ,x+d ,y+2*d ,fill = f)
        canvas.create_rectangle(x ,y ,x+d ,y+3*d ,fill = f)
        canvas.create_rectangle(x ,y ,x+d ,y+4*d ,fill = f)
        canvas.create_rectangle(x ,y ,x+d ,y+5*d ,fill = f)
        canvas.create_rectangle(x ,y ,x+d ,y+6*d ,fill = f)
        canvas.create_rectangle(x ,y ,x+d ,y+7*d ,fill = f)
        canvas.create_rectangle(x+3*d ,y+2*d ,x+4*d ,y+d ,fill = f)
        canvas.create_rectangle(x+4*d ,y+d ,x+5*d, y ,fill = f)
        canvas.create_rectangle(x+4*d ,y+2*d ,x+5*d, y+d ,fill = f)
        canvas.create_rectangle(x+4*d ,y+3*d ,x+5*d, y+d ,fill = f)
        canvas.create_rectangle(x+4*d ,y+4*d ,x+5*d, y+d ,fill = f)
        canvas.create_rectangle(x+4*d ,y+5*d ,x+5*d, y+d ,fill = f)
        canvas.create_rectangle(x+4*d ,y+6*d ,x+5*d, y+d ,fill = f)
        canvas.create_rectangle(x+4*d ,y+7*d ,x+5*d, y+d ,fill = f)
        #A
        canvas.create_rectangle(x+6*d ,y+2*d ,x+7*d ,y+d ,fill = f)
        canvas.create_rectangle(x+6*d ,y+3*d ,x+7*d ,y+d ,fill = f)
        canvas.create_rectangle(x+6*d ,y+4*d ,x+7*d ,y+d ,fill = f)
        canvas.create_rectangle(x+6*d ,y+5*d ,x+7*d ,y+d ,fill = f)
        canvas.create_rectangle(x+6*d ,y+6*d ,x+7*d ,y+d ,fill = f)
        canvas.create_rectangle(x+6*d ,y+7*d ,x+7*d ,y+d ,fill = f)
        canvas.create_rectangle(x+7*d ,y+d ,x+8*d ,y ,fill = f)
        canvas.create_rectangle(x+8*d ,y+d ,x+9*d ,y ,fill = f)
        canvas.create_rectangle(x+9*d ,y+d ,x+10*d ,y ,fill = f)
        canvas.create_rectangle(x+10*d ,y+2*d ,x+11*d ,y+d ,fill = f)
        canvas.create_rectangle(x+10*d ,y+3*d ,x+11*d ,y+2*d ,fill = f)
        canvas.create_rectangle(x+10*d ,y+4*d ,x+11*d ,y+3*d ,fill = f)
        canvas.create_rectangle(x+10*d ,y+5*d ,x+11*d ,y+4*d ,fill = f)
        canvas.create_rectangle(x+10*d ,y+6*d ,x+11*d ,y+5*d ,fill = f)
        canvas.create_rectangle(x+10*d ,y+7*d ,x+11*d ,y+6*d ,fill = f)
        canvas.create_rectangle(x+7*d ,y+4*d ,x+8*d ,y+3*d ,fill = f)
        canvas.create_rectangle(x+8*d ,y+4*d ,x+9*d ,y+3*d ,fill = f)
        canvas.create_rectangle(x+9*d ,y+4*d ,x+10*d ,y+3*d ,fill = f)
        #T
        canvas.create_rectangle(x+12*d ,y+d ,x+13*d ,y ,fill = f)
        canvas.create_rectangle(x+13*d ,y+d ,x+14*d ,y ,fill = f)
        canvas.create_rectangle(x+14*d ,y+d ,x+15*d ,y ,fill = f)
        canvas.create_rectangle(x+15*d ,y+d ,x+16*d ,y ,fill = f)
        canvas.create_rectangle(x+16*d ,y+d ,x+17*d ,y ,fill = f)
        canvas.create_rectangle(x+14*d ,y+2*d ,x+15*d ,y+d ,fill = f)
        canvas.create_rectangle(x+14*d ,y+3*d ,x+15*d ,y+2*d ,fill = f)
        canvas.create_rectangle(x+14*d ,y+4*d ,x+15*d ,y+3*d ,fill = f)
        canvas.create_rectangle(x+14*d ,y+5*d ,x+15*d ,y+4*d ,fill = f)
        canvas.create_rectangle(x+14*d ,y+6*d ,x+15*d ,y+5*d ,fill = f)
        canvas.create_rectangle(x+14*d ,y+7*d ,x+15*d ,y+6*d ,fill = f)
        #U
        canvas.create_rectangle(x+18*d ,y+d ,x+19*d ,y ,fill = f)
        canvas.create_rectangle(x+18*d ,y+2*d ,x+19*d ,y+d ,fill = f)
        canvas.create_rectangle(x+18*d ,y+3*d ,x+19*d ,y+2*d ,fill = f)
        canvas.create_rectangle(x+18*d ,y+4*d ,x+19*d ,y+3*d ,fill = f)
        canvas.create_rectangle(x+18*d ,y+5*d ,x+19*d ,y+4*d ,fill = f)
        canvas.create_rectangle(x+18*d ,y+6*d ,x+19*d ,y+5*d ,fill = f)
        canvas.create_rectangle(x+19*d ,y+7*d ,x+20*d ,y+6*d ,fill = f)
        canvas.create_rectangle(x+20*d ,y+7*d ,x+21*d ,y+6*d ,fill = f)
        canvas.create_rectangle(x+21*d ,y+7*d ,x+22*d ,y+6*d ,fill = f)
        canvas.create_rectangle(x+22*d ,y+6*d ,x+23*d ,y+5*d ,fill = f)
        canvas.create_rectangle(x+22*d ,y+5*d ,x+23*d ,y+4*d ,fill = f)
        canvas.create_rectangle(x+22*d ,y+4*d ,x+23*d ,y+3*d ,fill = f)
        canvas.create_rectangle(x+22*d ,y+3*d ,x+23*d ,y+2*d ,fill = f)
        canvas.create_rectangle(x+22*d ,y+2*d ,x+23*d ,y+d ,fill = f)
        canvas.create_rectangle(x+22*d ,y+d ,x+23*d ,y ,fill = f)
        #S
        canvas.create_rectangle(x+25*d ,y+d ,x+26*d ,y ,fill = f)
        canvas.create_rectangle(x+26*d ,y+d ,x+27*d ,y ,fill = f)
        canvas.create_rectangle(x+27*d ,y+d ,x+28*d ,y ,fill = f)
        canvas.create_rectangle(x+28*d ,y+d ,x+29*d ,y ,fill = f)
        canvas.create_rectangle(x+24*d ,y+2*d ,x+25*d ,y+d ,fill = f)
        canvas.create_rectangle(x+24*d ,y+3*d ,x+25*d ,y+2*d ,fill = f)
        canvas.create_rectangle(x+25*d ,y+4*d ,x+26*d ,y+3*d ,fill = f)
        canvas.create_rectangle(x+26*d ,y+4*d ,x+27*d ,y+3*d ,fill = f)
        canvas.create_rectangle(x+27*d ,y+4*d ,x+28*d ,y+3*d ,fill = f)
        canvas.create_rectangle(x+28*d ,y+5*d ,x+29*d ,y+4*d ,fill = f)
        canvas.create_rectangle(x+28*d ,y+6*d ,x+29*d ,y+5*d ,fill = f)
        canvas.create_rectangle(x+27*d ,y+7*d ,x+28*d ,y+6*d ,fill = f)
        canvas.create_rectangle(x+26*d ,y+7*d ,x+27*d ,y+6*d ,fill = f)
        canvas.create_rectangle(x+25*d ,y+7*d ,x+26*d ,y+6*d ,fill = f)
        canvas.create_rectangle(x+24*d ,y+7*d ,x+25*d ,y+6*d ,fill = f)
        x = x + dlzkaslova
    y = y + vyskaslova + vyskaslova // 2
    x = xx


canvas.mainloop()