#Calculator using TKINTER

from tkinter import *
import tkinter.messagebox


window = Tk()
window.title("Calculator")
window.geometry("300x400")
#adding buttons and other details

e= Entry(window, width=20,borderwidth=3)
e.place(x=10,y=10)

def click(num):
    result=e.get()
    e.delete(0,END)
    e.insert(0,str(result)+str(num))



b= Button(window,text="1",padx=5,pady=5,fg="blue",bg="red",command = lambda:click(1))
b.place(x=20,y=50)
b= Button(window,text="2",padx=5,pady=5,fg="blue",bg="red",command = lambda:click(2))
b.place(x=70,y=50)
b= Button(window,text="3",padx=5,pady=5,fg="blue",bg="red",command = lambda:click(3))
b.place(x=120,y=50)

b= Button(window,text="4",padx=5,pady=5,fg="blue",bg="red",command = lambda:click(4))
b.place(x=20,y=100)
b= Button(window,text="5",padx=5,pady=5,fg="blue",bg="red",command = lambda:click(5))
b.place(x=70,y=100)
b= Button(window,text="6",padx=5,pady=5,fg="blue",bg="red",command = lambda:click(6))
b.place(x=120,y=100)

b= Button(window,text="7",padx=5,pady=5,fg="blue",bg="red",command = lambda:click(7))
b.place(x=20,y=150)
b= Button(window,text="8",padx=5,pady=5,fg="blue",bg="red",command = lambda:click(8))
b.place(x=70,y=150)
b= Button(window,text="9",padx=5,pady=5,fg="blue",bg="red",command = lambda:click(9))
b.place(x=120,y=150)

b= Button(window,text="0",padx=5,pady=5,fg="blue",bg="red",command = lambda:click(0))
b.place(x=20,y=200)

def add():
    num1= e.get()
    global i
    i= int(num1)
    global math
    math="addition"
    e.delete(0,END)

b= Button(window,text="+",padx=5,pady=5,fg="blue",bg="red",command = add)
b.place(x=70,y=200)

def sub():
    num1= e.get()
    global i
    i= int(num1)
    global math
    math="subtraction"
    e.delete(0,END)

b= Button(window,text="-",padx=5,pady=5,fg="blue",bg="red",command = sub)
b.place(x=120,y=200)

def mul():
    num1= e.get()
    global i
    i= int(num1)
    global math
    math="multiplication"
    e.delete(0,END)

b= Button(window,text="*",padx=5,pady=5,fg="blue",bg="red",command = mul)
b.place(x=20,y=250)

def div():
    num1= e.get()
    global i
    i= int(num1)
    global math
    math="division"
    e.delete(0,END)
b= Button(window,text="/",padx=5,pady=5,fg="blue",bg="red",command = div)
b.place(x=70,y=250)

def eq():
    num2= int(e.get())
    e.delete(0,END)
    if math=="addition":
        e.insert(0,i + num2)
    elif math=="subtraction":
        e.insert(0,i - num2)
    elif math=="multiplication":
        e.insert(0,i * num2)
    elif math=="division":
        if num2 == 0:
            tkinter.messagebox.showerror('Divide Error',"division by zero is not possible")
        else:
          e.insert(0,i / num2)



b= Button(window,text="=",padx=5,pady=5,fg="blue",bg="red",command = eq)
b.place(x=120,y=250)

def clear():
    e.delete(0,END)

b= Button(window,text="Clear",padx=5,pady=5,fg="blue",bg="red",command = clear)
b.place(x=20,y=300)
mainloop()