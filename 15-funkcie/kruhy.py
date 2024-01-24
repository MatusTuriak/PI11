# import tkinter
# canvas = tkinter.Canvas()
# canvas.pack()
#
# def kruh(x, y, r, color):
#     canvas.create_oval(x - r, y - r, x + r,y + r, fill=color)
#
# def kruhy_riadok(x, y, pocet, r, farba):
#     for i in range(pocet):
#         kruh(x, y, r, farba)
#         x = x + 2 * r
#
#
#
# kruhy_riadok(50, 50, 10, 15, "red")
#
# canvas.mainloop()
import tkinter
canvas = tkinter.Canvas()
canvas.pack()

def kruh(x, y, r, color):
    canvas.create_oval(x - r, y - r, x + r,y + r, fill=color)

def kruhy_riadok(x, y, pocet, r, farba):
    for i in range(pocet):
            kruh(x, y, r, farba)
            x = x + 2 * r

def kruhy_stvorec(x, y, pocet, r, farba):
    for i in range(pocet):
        kruhy_riadok(x, y, pocet, r, farba)
        y = y + r * 2




kruhy_stvorec(50, 50, 10, 10, "red")

canvas.mainloop()