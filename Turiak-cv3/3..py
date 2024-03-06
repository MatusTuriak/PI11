import tkinter,random

canvas=tkinter.Canvas(width=500,height=500)
canvas.pack()

d = random.randint(150,200)
x = 10
y = 150
for i in range(10):
    farba = random.choice(("blue", "red", "green", "purple"))
    canvas.create_rectangle(x , y , x + 30, y + 30 , fill=farba)
    canvas.create_polygon(x , y, x + 15, y - 30, x + 30, y,fill=farba)
    x = x + 30



canvas.mainloop()