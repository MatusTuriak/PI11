import tkinter


canvas = tkinter.Canvas(width=300, height=300)
canvas.pack()

x = 3
y = 3
xx = x
d = 20
for i in range(298 // d): #riadky
    for j in range(298 // d): #stlpce
        canvas.create_oval(x , y + d , x + d, y)
        x = x + d
    y = y + d + 2
    x = xx


canvas.mainloop()