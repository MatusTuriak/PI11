import tkinter

canvas=tkinter.Canvas(width=500,height=500)
canvas.pack()


a = 10
b = 5

velkost = 30
farba1, farba2 = 'maroon', 'gold'
x = 10
y = 10
for i in range(b):
    f1, f2 = farba1, farba2
    for j in range(a):
        canvas.create_rectangle(x + (velkost+3) * j, y + (velkost+3) * i,
                                x + (velkost+3) * j + velkost, y + (velkost+3) * i + velkost,
                                fill=f1)
        f1, f2 = f2, f1
    farba1,farba2 = farba2,farba1

tkinter.mainloop()