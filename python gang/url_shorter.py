from tkinter import *
from turtle import width
import pyshorteners


def short():
    link = e1.get()
    short = pyshorteners.Shortener()
    x = short.tinyurl.short(link)
    print(x)
    e2.insert(0, x)

app = Tk()

app.geometry("500x300")

l1 = Label(app, text="MY SHORTER APP", font=1)
l2 = Label(app, text="ENTER URL", font=0, width=10)
e1 = Entry(app, width=50)
btn = Button(app, text="short", width= 10, height=1, command=short)
e2 = Entry(app, text = '', font=0 )

l1.pack(ipady=20)
l2.pack()
e1.pack()
btn.pack(pady=10)
e2.pack()

# l1.grid(row=0, column=0, columnspan=3, ipady=20)
# l2.grid(row=1, column=0, ipadx=1)
# e1.grid(row=1, column=1, columnspan=1)
# btn.grid(row=3, column=0)
# e2.grid(row=3, column=1)

app.mainloop()
