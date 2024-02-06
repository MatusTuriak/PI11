#import tkinter
#import random
#
#canvas=tkinter.Canvas(width=600,height=500)
#canvas.pack()
#x = 3
#xx = x
#y = 10
#d = 30
#stvrtina = d // 4
#for j in range(498 // d):
#    for i in range(598 // d):
#        farba = random.choice(("green","blue","yellow","red"))
#        canvas.create_rectangle(x , y + d//2 ,x + d ,y + d+2*stvrtina,fill=farba)
#        canvas.create_rectangle(x+stvrtina ,y+3*stvrtina ,x+3*stvrtina, y + d+stvrtina,fill="white")
#        canvas.create_line(x+stvrtina ,y+3*stvrtina ,x +3*stvrtina,y+d+stvrtina)
#        canvas.create_line(x+stvrtina ,y+d+stvrtina,x+3*stvrtina ,y+3*stvrtina)
#        canvas.create_polygon(x,y+d//2,x+d/2,y+stvrtina,x+d,y+d//2,fill=farba)
#        x = x + d
#    y = y + d + d // 2
#    x = xx
#
#
#canvas.mainloop()

#import tkinter
#
#canvas = tkinter.Canvas()
#canvas.pack()
#
#n = 13
#for i in range(n):
#    for j in range(n):
#        x = j*20 + 100
#        y = i*20 + 12
#        if i == 6:
#            farba = 'red'
#        elif j == 6:
#            farba = "red"
#        else:
#            farba = 'white'
#        canvas.create_oval(x - 8, y - 8, x + 8, y + 8, fill=farba)
#
#tkinter.mainloop()
# import random
# from math import pi
#
# r = 12
# o = 2 * pi * r
# print(round(o , 2))
#
# cislo = random.randrange(0,10)
# farba = random.choice(("red","blue","green"))
# print(cislo)
# print(farba)

# import tkinter,time,random
# canvas = tkinter.Canvas()
# canvas.pack()
#
#
# stvorec1 = canvas.create_rectangle(10,10,110,110, fill="red")
# for i in range(250):
#     canvas.update()
#     time.sleep(0.01)
#     canvas.move(stvorec1, 1, 0)
#     farba = random.choice(("red", "blue", "purple"))
#     canvas.itemconfig(stvorec1, fill=farba)
#
# canvas.mainloop()

# import tkinter,random
#
# canvas = tkinter.Canvas(width=500,height=500)
# canvas.pack()
#
# polom = 10
# for i in range(20):
#     x = random.randint(2,480)
#     y = random.randint(2,480)
#     r = random.randint(0,250)
#     g = random.randint(0,250)
#     b = random.randint(0,250)
#     farba = f"#{r:02x}{g:02x}{b:02x}"
#     canvas.create_oval(x - polom,y - polom,x + polom,y + polom, fill=farba)
#
# canvas.mainloop()
# max_bodov = 30
# pocet_bodov = int(input("zadaj pocet bodov: "))
# percenta = (pocet_bodov / max_bodov * 100)
# print(f"ziskal si {round(percenta, 2)}%")
# if percenta >= 90:
#     print("vyborny")
# elif percenta <= 75:
#     print("chvalitebny")
# elif percenta <= 50:
#     print("dobry")
# elif percenta <= 30:
#     print("dostatocny")
# else:
#     print("nedostatocny")
# import tkinter
#
# canvas=tkinter.Canvas(width=500,height=500)
# canvas.pack()
#
# d = 20
# x = 1
# y = 1
# a = 1
# b = 1
# farba1 = "red"
# farba2 = "blue"
# for i in range (30):
#     canvas.create_line(x , y ,x ,y + 500, fill=farba1)
#     x = x + d
#     farba1, farba2 = farba2, farba1
# for j in range(30):
#     canvas.create_line(a ,b , a + 500, b, fill=farba2)
#     b = b + d
#     farba1,farba2=farba2,farba1
#
# canvas.mainloop()
# import tkinter
# import random
# canvas_width = 500
# canvas_height = 500
# pocet = 1000
# polomer = 10
#
# canvas = tkinter.Canvas(bg='white', width=canvas_width, height=canvas_height)
# canvas.pack()
#
# for i in range(pocet):
#     x = random.randint(polomer + 2, canvas_width - polomer)
#     y = random.randint(polomer + 2, canvas_height - polomer - 2)
#     if x < canvas_width // 2 and y < canvas_height // 2:
#         farba = 'red'
#     elif x < canvas_width // 2 and y >= canvas_height // 2:
#         farba = 'yellow'
#     elif x > canvas_width // 2 and y < canvas_height // 2:
#         farba = "blue"
#     else:
#         farba = "green"
#     canvas.create_oval(x - polomer, y - polomer, x + polomer, y + polomer, fill=farba,)
#
# tkinter.mainloop()