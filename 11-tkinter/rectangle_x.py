import tkinter

canvas = tkinter.Canvas()
canvas.pack()

x = 10
y = 10
d = 20
farba = "blue"
canvas.create_rectangle(x, y, x+d, y+d, fil=farba)
canvas.create_rectangle(x+d, y+d, x+2*d, y+2*d, fill=farba)
canvas.create_rectangle(x+2*d, y+2*d, x+3*d, y+3*d, fill=farba)
canvas.create_rectangle(x+3*d, y+2*d, x+4*d, y+d, fill="green")
canvas.create_rectangle(x+4*d, y+d, x+5*d, y, fil=farba)
canvas.create_rectangle(x+d, y+4*d, x+2*d, y+3*d, fill=farba)
canvas.create_rectangle(x, y+5*d, x+d, y+4*d, fill=farba)
canvas.create_rectangle(x+3*d, y+3*d, x+4*d, y+4*d, fill=farba)
canvas.create_rectangle(x+4*d, y+4*d, x+5*d, y+5*d, fill=farba)

x = 6 * d
y = 10
farba = "red"
canvas.create_rectangle(x, y, x+d, y+d, fil=farba)
canvas.create_rectangle(x+d, y+d, x+2*d, y+2*d, fill=farba)
canvas.create_rectangle(x+2*d, y+2*d, x+3*d, y+3*d, fill=farba)
canvas.create_rectangle(x+3*d, y+2*d, x+4*d, y+d, fill=farba)
canvas.create_rectangle(x+4*d, y+d, x+5*d, y, fil=farba)
canvas.create_rectangle(x+d, y+4*d, x+2*d, y+3*d, fill=farba)
canvas.create_rectangle(x, y+5*d, x+d, y+4*d, fill=farba)
canvas.create_rectangle(x+3*d, y+3*d, x+4*d, y+4*d, fill=farba)
canvas.create_rectangle(x+4*d, y+4*d, x+5*d, y+5*d, fill=farba)


canvas.mainloop()