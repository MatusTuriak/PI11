import tkinter,random

canvas=tkinter.Canvas(width=500,height=500)
canvas.pack()

polomer = 10
for i in range(2000):
    x = random.randint(10,350)
    y = random.randint(10,250)
    if y <= 90:
        farba = "black"
    elif y <= 170:
        farba = "red"
    else:
        farba = "gold"
    canvas.create_oval(x - polomer, y - polomer, x + polomer, y + polomer, fill=farba)

canvas.mainloop()