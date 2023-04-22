from tkinter import *
x = Tk()
x.geometry("400x300")

x.title("Simple Calculator")

e = Entry(x,width = 30)
e.grid(columnspan=4,padx=5,pady=5)

def click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number))

def clearfunc():
    e.delete(0,END)

def addfunc():
    num1 = e.get()
    global f_num1
    global math
    math = "addition"
    f_num1 = int(num1)
    e.delete(0,END)

def multiplyfunc():
    num1 = e.get()
    global f_num1
    global math
    math = "multiplication"
    f_num1 = int(num1)
    e.delete(0,END)

def dividefunc():
    num1 = e.get()
    global f_num1
    global math
    math = "division"
    f_num1 = int(num1)
    e.delete(0,END)

def subtractfunc():
    num1 = e.get()
    global f_num1
    global math
    math = "subtraction"
    f_num1 = int(num1)
    e.delete(0,END)

def equalfunc():
    num2 = e.get()
    e.delete(0,END)
    if math == "addition":
        e.insert(0,f_num1 + int(num2))
    
    if math == "subtraction":
        e.insert(0,f_num1 - int(num2))

    if math == "multiplication":
        e.insert(0,f_num1 * int(num2))

    if math == "division":
        e.insert(0,f_num1 / int(num2))

button1 = Button(x,text="1",padx=40,pady=20,command =lambda: click(1))
button2 = Button(x,text="2",padx=40,pady=20,command =lambda: click(2))
button3 = Button(x,text="3",padx=40,pady=20,command =lambda: click(3))
button4 = Button(x,text="4",padx=40,pady=20,command =lambda: click(4))
button5 = Button(x,text="5",padx=40,pady=20,command =lambda: click(5))
button6 = Button(x,text="6",padx=40,pady=20,command =lambda: click(6))
button7 = Button(x,text="7",padx=40,pady=20,command =lambda: click(7))
button8 = Button(x,text="8",padx=40,pady=20,command =lambda: click(8))
button9 = Button(x,text="9",padx=40,pady=20,command =lambda: click(9))
button0 = Button(x,text="0",padx=40,pady=20,command =lambda: click(0))
add = Button(x,text="+",fg = "red",padx=40,pady=20,command =lambda: addfunc())
equal = Button(x,text="=",fg = "blue",padx=40,pady=20,command =lambda: equalfunc())
clear = Button(x,text="Clear",fg = "blue",padx=40,pady=20,command =lambda: clearfunc())
multiply = Button(x,text="*",fg = "red",padx=40,pady=20,command =lambda: multiplyfunc())
divide = Button(x,text="/",fg = "red",padx=40,pady=20,command =lambda: dividefunc())
subtract = Button(x,text="-",fg = "red",padx=40,pady=20,command =lambda: subtractfunc())

button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button7.grid(row=3,column=0)
button8.grid(row=3,column=1)
button9.grid(row=3,column=2)
button0.grid(row=4,column=0)
add.grid(row=1,column=3)
equal.grid(row=4,column=2)
clear.grid(row=4,column=1)
multiply.grid(row=3,column=3)
divide.grid(row=4,column=3)
subtract.grid(row=2,column=3)

x.mainloop()