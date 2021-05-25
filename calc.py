from tkinter import *


class Calc:

    def __init__(self):
        self.window = Tk()
        self.window.title("Calculator")
        self.window.resizable(0, 0)

        self.screen_numbers = Entry(self.window, font='arial 30 bold', bg="#1d2f38", fg="white", width=18)
        self.screen_numbers.pack()

        self.frame = Frame(self.window)
        self.frame.pack()

        self.button_1 = Button(self.frame, bg="orange", bd=0, text="1", font="arial 20 bold", fg="black", width=5,
                               height=3, command=None)
        self.button_2 = Button(self.frame, bg="orange", bd=0, text="2", font="arial 20 bold", fg="black", width=5,
                               height=3, command=None)
        self.button_3 = Button(self.frame, bg="orange", bd=0, text="3", font="arial 20 bold", fg="black", width=5,
                               height=3, command=None)
        self.button_4 = Button(self.frame, bg="orange", bd=0, text="4", font="arial 20 bold", fg="black", width=5,
                               height=3, command=None)
        self.button_5 = Button(self.frame, bg="orange", bd=0, text="5", font="arial 20 bold", fg="black", width=5,
                               height=3, command=None)
        self.button_6 = Button(self.frame, bg="orange", bd=0, text="6", font="arial 20 bold", fg="black", width=5,
                               height=3, command=None)
        self.button_7 = Button(self.frame, bg="orange", bd=0, text="7", font="arial 20 bold", fg="black", width=5,
                               height=3, command=None)
        self.button_8 = Button(self.frame, bg="orange", bd=0, text="8", font="arial 20 bold", fg="black", width=5,
                               height=3, command=None)
        self.button_9 = Button(self.frame, bg="orange", bd=0, text="9", font="arial 20 bold", fg="black", width=5,
                               height=3, command=None)
        self.button_0 = Button(self.frame, bg="orange", bd=0, text="0", font="arial 20 bold", fg="black", width=5,
                               height=3, command=None)
        self.button_00 = Button(self.frame, bg="orange", bd=0, text="00", font="arial 20 bold", fg="black", width=5,
                               height=3, command=None)
        self.button_dot = Button(self.frame, bg="orange", bd=0, text=".", font="arial 20 bold", fg="black", width=5,
                               height=3, command=None)
        self.button_increase = Button(self.frame, bg="orange", bd=0, text="+", font="arial 20 bold", fg="black",
                                 width=5, height=3, command=None)
        self.button_unincrease = Button(self.frame, bg="orange", bd=0, text="-", font="arial 20 bold", fg="black",
                                 width=5, height=3, command=None)
        self.button_division = Button(self.frame, bg="orange", bd=0, text="/", font="arial 20 bold", fg="black",
                                 width=5, height=3, command=None)
        self.button_multi = Button(self.frame, bg="orange", bd=0, text="*", font="arial 20 bold", fg="black",
                                 width=5, height=3, command=None)
        self.button_clean = Button(self.frame, bg="orange", bd=0, text="AC", font="arial 20 bold", fg="black",
                                 width=5, height=3, command=None)
        self.button_equal = Button(self.frame, bg="orange", bd=0, text="=", font="arial 20 bold", fg="black",
                                 width=19, height=3, command=None)



        self.button_1.grid(row=0, column=0)
        self.button_2.grid(row=0, column=1)
        self.button_3.grid(row=0, column=2)
        self.button_clean.grid(row=0, column=3)
        self.button_4.grid(row=1, column=0)
        self.button_5.grid(row=1, column=1)
        self.button_6.grid(row=1, column=2)
        self.button_increase.grid(row=1, column=3)
        self.button_7.grid(row=2, column=0)
        self.button_8.grid(row=2, column=1)
        self.button_9.grid(row=2, column=2)
        self.button_unincrease.grid(row=2, column=3)
        self.button_0.grid(row=3, column=0)
        self.button_00.grid(row=3, column=1)
        self.button_dot.grid(row=3, column=2)
        self.button_multi.grid(row=3, column=3)
        self.button_equal.grid(row=4, column=0, columnspan=3)
        self.button_division.grid(row=4, column=3)

        self.window.mainloop()


Calc()
