import tkinter
import random
canvas_width = 500
canvas_height = 500
pocet = 1000
polomer = 10

canvas = tkinter.Canvas(bg='white', width=canvas_width, height=canvas_height)
canvas.pack()

for i in range(pocet):
    x = random.randint(polomer + 2, canvas_width - polomer)
    y = random.randint(polomer + 2, canvas_height - polomer - 2)
    if x < canvas_width // 2 and y < canvas_height // 2:
        farba = 'red'
    elif x < canvas_width // 2 and y >= canvas_height // 2:
        farba = 'yellow'
    elif x > canvas_width // 2 and y < canvas_height // 2:
        farba = "blue"
    else:
        farba = "green"
    canvas.create_oval(x - polomer, y - polomer, x + polomer, y + polomer, fill=farba,)

tkinter.mainloop()