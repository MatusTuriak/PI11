import tkinter

canvas = tkinter.Canvas()
canvas.pack()

d = 13
for i in range(d):
    for j in range(d):
        x = j*20 + 100
        y = i*20 + 12
        if i == 6:
            farba = 'red'
        elif j == 6:
            farba = "red"
        else:
            farba = 'white'
        canvas.create_oval(x - 8, y - 8, x + 8, y + 8, fill=farba)

tkinter.mainloop()