import tkinter

canvas = tkinter.Canvas()
canvas.pack()
x = 2
y = 2
dlzka = 50
canvas.create_rectangle(x, y, x + dlzka, y + dlzka, fill="red") # vytvor stvorec
canvas.create_rectangle(x + dlzka, y, x + (2*dlzka), y + dlzka)
canvas.create_rectangle(x + (2*dlzka), y, x + (3*dlzka), y + dlzka)
canvas.create_oval(x + dlzka, y + dlzka, x + (2*dlzka), y + (2*dlzka)) # vytvor kruh
canvas.create_oval(x + dlzka, y + (2*dlzka), x + (2*dlzka), y + (3*dlzka))
canvas.create_rectangle(x + dlzka, y + (3*dlzka), x + (2*dlzka), y + (4*dlzka))
canvas.create_rectangle(x, y + (3*dlzka), x + dlzka, y + (4*dlzka))
canvas.create_rectangle(x + (2*dlzka), y + (3*dlzka), x + (3*dlzka), y + (4*dlzka))
canvas.mainloop()