import tkinter, time, random

canvas_width = 500
canvas_height = 600
santa_x = canvas_width // 2
santa_y = 66
santa_posun = 2

canvas = tkinter.Canvas(width=canvas_width, height=canvas_height)
image_santa = tkinter.PhotoImage(file="santa.png.png")
santa = canvas.create_image(santa_x, santa_y,  image=image_santa)
santa2 = canvas.create_image(santa_x - 128, santa_y,  image=image_santa)
santa3 = canvas.create_image(santa_x + 128, santa_y,  image=image_santa)
canvas.pack()
for i in range(250):
    canvas.update()
    time.sleep(0.01)
    canvas.move(santa3, 0, santa_posun)

while True:
    canvas.update()
    time.sleep(0.01)
    canvas.move(santa, 0, santa_posun)
    santa_y = santa_y + santa_posun
    if santa_y == canvas_height + 64:
        canvas.delete(santa)
        santa_y = 66
        santa = canvas.create_image(santa_x, santa_y, image=image_santa)








