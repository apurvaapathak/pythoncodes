from tkinter import *

box = Tk()
box.title("Login Page!!")
box.resizable(5, 5)

f1 = Frame(box)
f2 = Frame(box)
f1.pack()
f2.pack()

l1 = Label(f1, text="Username: ")
l1.pack(side="left")

l2 = Label(f2, text="Password: ")
l2.pack(side="left")

e1 = Entry(f1, width=20)
e1.pack()

e2 = Entry(f2, width=20)
e2.pack()
e2.config(show="*")


def action():
    us = e1.get()
    ps = e2.get()
    print(f"Welcome {us}!! Your password is {ps}.")
    e1.delete(0, END)
    e2.delete(0, END)


b = Button(box, text="Login", bg='green', fg='black', command=action)
b.pack(side="bottom", padx=10, pady=10)

box.mainloop()



