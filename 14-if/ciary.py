import tkinter
canvas_width = 500
canvas_height = 500
d = 20
x = 1
y = 1
a = 1
b = 1
farba1 = "red"
farba2 = "blue"

canvas = tkinter.Canvas(bg="white", width=canvas_width, height=canvas_height)
canvas.pack()

for i in range(30):
    canvas.create_line(x , y  , x , y + canvas_height,width= 3, fill=farba1)
    x = x + d
    farba1, farba2 = farba2,farba1
for j in range(30):
    canvas.create_line(a , b , a + canvas_width, b,width=3, fill= farba2)
    b = b + d
    farba1, farba2 = farba2, farba1


tkinter.mainloop()