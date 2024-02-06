import tkinter

def rgb(r, g, b):
    return f"#{r:02x}{g:02x}{b:02x}"
def stvorce(x, y, pocet, dlzka, r=255, g=255, b=255):
    for i in range(pocet):
        krok = 255 // pocet
        canvas.create_rectangle(x, y, x+dlzka,y+dlzka, fill=rgb(r, g, b))


        x += dlzka
        if r > krok:
            r -= krok
        if g > krok:
            g -= krok
        if b > krok:
            b -= krok



canvas = tkinter.Canvas(width = 600)
canvas.pack()

for i in range(3):
    stvorce(50, 50 + 20, 20, 20, 255, 0, 0)
    stvorce(50, 70 + 40, 20, 20, 0, 255, 0)
    stvorce(50, 90 + 60, 20, 20, 0, 0, 255)



       # x,  y, pocet, dlzka

tkinter.mainloop()