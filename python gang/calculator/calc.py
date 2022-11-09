
from tkinter import *

screen = Tk()

screen.title("calculator")
screen.geometry("480x570")
screen.config(bg="black")

enter_text = Entry(screen, width=30, font=("ariel", "20"))

btn_1 = Button(screen, text='1', bg="white",height=3, width=5, font=("ariel", "15"))
btn_2 = Button(screen, text='2', height=3, bg="white", width=5, font=("ariel", "15"))
btn_3 = Button(screen, text='3', height=3, bg="white", width=5, font=("ariel", "15"))
btn_4 = Button(screen, text='4', height=3, bg="white", width=5, font=("ariel", "15"))
btn_5 = Button(screen, text='5', height=3, width=5, bg="white", font=("ariel", "15"))
btn_6 = Button(screen, text='6', height=3, width=5, bg="white",font=("ariel", "15"))
btn_7 = Button(screen, text='7', height=3, width=5,bg="white", font=("ariel", "15"))
btn_8 = Button(screen, text='8', height=3, width=5,bg="white", font=("ariel", "15"))
btn_9 = Button(screen, text='9', height=3, width=5,bg="white", font=("ariel", "15"))
btn_0 = Button(screen, text='0', height=3, width=5,bg="white", font=("ariel", "15"))

minus = Button(screen, text='-', height=3, width=5, bg="white", font=("ariel", "15"))
plus = Button(screen, text='+', height=3, width=5, bg="white", font=("ariel", "15"))
multi = Button(screen, text='x', height=3, width=5, bg="white",font=("ariel", "15"))
div = Button(screen, text='/', height=3, width=5, bg="white", font=("ariel", "15"))
equal = Button(screen, text='=', height=3, width=5, bg="white", font=("ariel", "15"))
clr = Button(screen, text='C', height=3, width=5,bg="white", font=("ariel", "15"))
dot = Button(screen, text='.', height=3, width=5, bg="white", font=("ariel", "15")  )

#######################################

enter_text.grid(row=0, column=0, columnspan=4, ipady=15, pady=15)

btn_7.grid(row=3, column=0, ipadx=15, pady=10, padx=10, ipady=5)
btn_8.grid(row=3, column=1, ipadx=15, pady=10, padx=10, ipady=5)
btn_9.grid(row=3, column=2, ipadx=15, pady=10, padx=10, ipady=5)

btn_4.grid(row=4, column=0, ipadx=15, pady=10, padx=10, ipady=5)
btn_5.grid(row=4, column=1, ipadx=15, pady=10, padx=10, ipady=5)
btn_6.grid(row=4, column=2, ipadx=15, pady=10, padx=10, ipady=5)

btn_1.grid(row=5, column=0, ipadx=15, pady=10, padx=10, ipady=5)
btn_2.grid(row=5, column=1, ipadx=15, pady=10, padx=10, ipady=5)
btn_3.grid(row=5, column=2, ipadx=15, pady=10, padx=10, ipady=5)
btn_0.grid(row=6, column=1, ipadx=15, pady=10, padx=10, ipady=5)
dot.grid(row=6, column=0, ipadx=15, pady=10, padx=10, ipady=5)
equal.grid(row=6, column=2, ipadx=15, pady=10, padx=10, ipady=5)

minus.grid(row=3, column=3, ipadx=15, pady=10, padx=10, ipady=5)
plus.grid(row=4, column=3, ipadx=15, pady=10, padx=10, ipady=5)
div.grid(row=5, column=3, ipadx=15, pady=10, padx=10, ipady=5)
multi.grid(row=6, column=3, ipadx=15, pady=10, padx=10, ipady=5)


screen.mainloop()