from tkinter import*
root=Tk()
root.iconbitmap("cc.ico")

root.title("Simple calculator")
root.configure(bg="gray")


e=Entry(root,width=15,borderwidth=5,font=("arial bold",20))
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def button_click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def button_clear():
    e.delete(0,END)

def button_add():
    first_number=e.get()
    global f_num
    global math
    math="add"
    f_num=int(first_number)
    e.delete(0,END)


def button_sub():
    first_number=e.get()
    global f_num
    global math
    math = "sub"
    f_num=int(first_number)
    e.delete(0,END)


def button_mul():
    first_number=e.get()
    global f_num
    global math
    math = "mul"
    f_num=int(first_number)
    e.delete(0,END)

def button_div():
    first_number=e.get()
    global f_num
    global math
    math = "div"
    f_num=int(first_number)
    e.delete(0,END)


def button_equal():
    second_number = e.get()
    e.delete(0,END)
    if math=="add":
        e.insert(0, f_num + int(second_number))
    if math == "sub":
        e.insert(0, f_num - int(second_number))
    if math == "mul":
        e.insert(0, f_num * int(second_number))
    if math == "div":
        e.insert(0, f_num / int(second_number))

def delete_number():
    current=e.get()
    length=len(current)-1
    e.delete(length,END)

def button_exit():
    root.destroy()



button_del=Button(root,text="RM",padx=40,pady=10,command=delete_number)
button_1=Button(root,text="1",padx=40,pady=20,command=lambda :button_click(1),border="5",bg='moccasin')
button_2=Button(root,text="2",padx=40,pady=20,command=lambda :button_click(2),border="5",bg='moccasin')
button_3=Button(root,text="3",padx=40,pady=20,command=lambda :button_click(3),border="5",bg='moccasin')
button_4=Button(root,text="4",padx=40,pady=20,command=lambda :button_click(4),border="5",bg='moccasin')
button_5=Button(root,text="5",padx=40,pady=20,command=lambda :button_click(5),border="5",bg='moccasin')
button_6=Button(root,text="6",padx=40,pady=20,command=lambda :button_click(6),border="5",bg='moccasin')
button_7=Button(root,text="7",padx=40,pady=20,command=lambda :button_click(7),border="5",bg='moccasin')
button_8=Button(root,text="8",padx=40,pady=20,command=lambda :button_click(8),border="5",bg='moccasin')
button_9=Button(root,text="9",padx=40,pady=20,command=lambda :button_click(9),border="5",bg='moccasin')
button_0=Button(root,text="0",padx=40,pady=20,command=lambda :button_click(0),border="5",bg='moccasin')
button_add=Button(root,text="+",padx=39,pady=20,command=button_add,border="5",bg='lightcyan')
button_sub=Button(root,text="-",padx=39,pady=20,command=button_sub,border="5",bg='lightcyan')
button_mul=Button(root,text="*",padx=39,pady=20,command=button_mul,border="5",bg='lightcyan')
button_div=Button(root,text="/",padx=39,pady=20,command=button_div,border="5",bg='lightcyan')
button_equal=Button(root,text="=",padx=90,pady=20,command=button_equal,fg="black",bg="aquamarine",border="5")
button_clear=Button(root,text="Clear",padx=180,pady=8,command=button_clear,border="5",bg="honeydew")
button_exit=Button(root,text="exit",padx=40,pady=5,command=button_exit,border="5",bg="honeydew")


button_del.grid(row=0,column=4)
button_1.grid(row=4,column=0)
button_2.grid(row=4,column=1)
button_3.grid(row=4,column=2)

button_4.grid(row=3,column=0)
button_5.grid(row=3,column=1)
button_6.grid(row=3,column=2)

button_7.grid(row=2,column=0)
button_8.grid(row=2,column=1)
button_9.grid(row=2,column=2)

button_0.grid(row=5,column=0)
button_clear.grid(row=1,column=0,columnspan=5)
button_add.grid(row=2,column=4)
button_sub.grid(row=3,column=4)
button_mul.grid(row=4,column=4)
button_div.grid(row=5,column=4)
button_equal.grid(row=5,column=1,columnspan=2)
button_exit.grid(row=6,column=0,columnspan=5)



root.mainloop()



