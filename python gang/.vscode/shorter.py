
""" https://drive.google.com/drive/u/0/folders/1H4W-EcPSYSldIJRvAIY2Q1i7SxkIvYmV """


from tkinter import *
import pyshorteners


def shorter():

    link = entry_1.get()

    short = pyshorteners.Shortener()

    x = short.tinyurl.short(link)

    lavel_2.config(text=x)
    


app = Tk()

app.geometry("300x300")

lavel_1 = Label(app, text="ENTER LINK", font=1)
entry_1 = Entry(app, fg="yellow", bg="blue", width=50)
lavel_2 = Label(app, width=50)
btn = Button(app, text="shorter", command=shorter)


lavel_1.pack()
entry_1.pack()
btn.pack()
lavel_2.pack()


app.mainloop()













