
from tkinter import *
root = Tk()
e = Entry(root, width=50, borderwidth=5)
e.grid(row=0,column=0, columnspan=3, padx=10, pady=10)
def click(number):
    global current
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
def clear():
    e.delete(0, END)
def add():
    global math
    global fnum
    current = e.get()
    fnum = int(current)
    math = "addition"
    
    e.delete(0, END)
def equal():
    if math == "addition":
        secondnumber = e.get()
        e.delete(0, END)
        e.insert(0,fnum + int(secondnumber))
    
    

button1 = Button(root, text="1", padx=30, pady=30, command=lambda: click(1))
button2 = Button(root, text="2", padx=30, pady=30, command=lambda: click(2))
button3 = Button(root, text="3", padx=30, pady=30, command=lambda: click(3))
button4 = Button(root, text="4", padx=30, pady=30, command=lambda: click(4))
button5 = Button(root, text="5", padx=30, pady=30, command=lambda: click(5))
button6 = Button(root, text="6", padx=30, pady=30, command=lambda: click(6))
button7 = Button(root, text="7", padx=30, pady=30, command=lambda: click(7))
button8 = Button(root, text="8", padx=30, pady=30, command=lambda: click(8))
button9 = Button(root, text="9", padx=30, pady=30, command=lambda: click(9))
button0 = Button(root, text="0", padx=30, pady=30, command=lambda: click(0))
buttonclear = Button(root, text="clear", padx=30, pady=30, command=clear)
buttonadd = Button(root, text="+", padx=30, pady=30, command=add)
buttonsubtract = Button(root, text="-", padx=30, pady=30, command=lambda: click(0))
buttonequal = Button(root, text="=", padx=30, pady=30, command=equal)


button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)

button0.grid(row=4, column=0)
buttonadd.grid(row=4, column=1)
buttonsubtract.grid(row=4, column=2)

buttonclear.grid(row=5, column=0)
buttonequal.grid(row=5, column=1)

