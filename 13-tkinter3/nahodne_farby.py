import tkinter, random

canvas = tkinter.Canvas(width = 500, height = 500)
canvas.pack()

meno = "Ján"
priezvisko = "Mrkvička"
vek = 255

print("Volám sa ",meno," ", priezvisko)
print(f"Volám sa {meno} {priezvisko} a mám {vek:02x} rokov.")# vek:02x, 02 je pocet cifier a x prevedie do 16tkovej sustavy

r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)
farba = f"#{r:02x}{g:02x}{b:02x}"

polom = 10
for i in range(20):
    x = random.randint(2, 480)
    y = random.randint(2, 480)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    farba = f"#{r:02x}{g:02x}{b:02x}"
    canvas.create_oval(x - polom , y - polom, x + polom ,y + polom, fill=farba)

canvas.mainloop()
x