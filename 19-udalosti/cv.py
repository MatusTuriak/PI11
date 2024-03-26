#1.
# import tkinter
#
# def kresli(event):
#     x, y = event.x, event.y
#     canvas.create_line(x, y, x + 100, y, width=2)
#
# def zmaz(event=None):
#     canvas.delete('all')
#
# canvas = tkinter.Canvas()
# canvas.pack()
#
# canvas.bind('<B1-Motion>', kresli)
# canvas.bind('<ButtonPress-3>', zmaz)
# tkinter.Button(text='Zmaž', command=zmaz).pack()
#
# tkinter.mainloop()

#2.
# import tkinter
# import random
#
# r = 1
# farba = 'yellow'
#
# def kresli(event):
#     global r
#     x, y = event.x, event.y
#     canvas.create_oval(x - r, y - r, x + r, y + r, fill=farba)
#     r += .1
#
# def zmaz(event):
#     global r
#     r = 1
#     canvas.delete('all')
#
# def zmen_farbu():
#     global farba
#     farba = f'#{random.randrange(256**3):06x}'
#
# canvas = tkinter.Canvas()
# canvas.pack()
#
# canvas.bind('<B1-Motion>', kresli)
# canvas.bind('<ButtonPress-3>', zmaz)
# tkinter.Button(text='Zmeň farbu', command=zmen_farbu).pack()
#
# tkinter.mainloop()

#3.
# import tkinter
# import random
#
# zoznam = []
#
# def k(event):
#     zoznam.append((event.x, event.y))
#     if len(zoznam) == 2:
#         fill = f'#{random.randrange(256**3):06x}'
#         canvas.create_rectangle(zoznam, fill=fill)
#         zoznam.clear()
#
# canvas = tkinter.Canvas()
# canvas.pack()
#
# canvas.bind('<ButtonPress>', k)
#
# tkinter.mainloop()

#4.
# import tkinter
# import random
#
# zoznam = []
#
# def klik(event):
#     xy = event.x, event.y
#     zoznam.append(xy)
#     canvas.create_text(xy, text='+')
#     if len(zoznam) == 3:
#         fill = f'#{random.randrange(256**3):06x}'
#         canvas.create_polygon(zoznam, fill=fill)
#         zoznam.pop(0)
#
# canvas = tkinter.Canvas()
# canvas.pack()
#
# canvas.bind('<ButtonPress-1>', klik)
#
# tkinter.mainloop()

#6.
# import tkinter
# import random
#
# zoznam = []       # momentálne vytvarané vrcholy
# polygony = []     # všetky nakreslené polygóny
#
# def klik(event):
#     x, y = event.x, event.y
#     zoznam.append((x, y))
#     canvas.create_text(x, y, text='+', tag='+')
#     x0, y0 = zoznam[0]
#     if len(zoznam) > 2 and (x - x0) ** 2 + (y - y0) ** 2 < 25:
#         fill = f'#{random.randrange(256**3):06x}'
#         polygony.append(canvas.create_polygon(zoznam, fill=fill))
#         zoznam.clear()
#         canvas.delete('+')
#
# def zmaz():
#     canvas.delete('all')
#     zoznam.clear()
#     polygony.clear()
#
# def zmen_farbu():
#     if polygony:
#         fill = f'#{random.randrange(256**3):06x}'
#         canvas.itemconfig(polygony[-1], fill=fill)
#
# def spat():
#     if polygony:
#         canvas.delete(polygony.pop(0))
#
# canvas = tkinter.Canvas()
# canvas.pack(side='left')
#
# canvas.bind('<ButtonPress-1>', klik)
# tkinter.Button(text='Zmaž', command=zmaz).pack()
# tkinter.Button(text='Zmeň farbu', command=zmen_farbu).pack()
# tkinter.Button(text='Späť', command=spat).pack()
#
# tkinter.mainloop()