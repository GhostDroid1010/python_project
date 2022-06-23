#clock

from tkinter import *
import time
import random


def lol():
    op= time.strftime("%H:%M:%S")
    l2.config(text=op)
    l2.after(200, lol)


greeting=["hello","hii","hey","oye"]
t1=["here is your time","this is your time","look at your time","look at to your time"]

g=random.choice(greeting)
t=random.choice(t1)


print("hello")
name1=input("what is your name? -->")
name=(f"{g} {name1} {t}")


print("enter your password")
password=input("(^_^)-->")

if password=="12345":

    print("accepted")
    print("have a nice day!")


    root = Tk()

    root.title("digital clock")
    root.geometry("600x300")
    root.resizable("false", "false")
    root.config(bg=("yellow"))

    l1 = Label(root, text=("time"), font=("mincho", "50", "bold",), fg=("red"), bg="lightblue", borderwidth=5,relief=("sunken"))
    l1.pack()

    l3 = Label(root, text=(), font=("mincho", "30", "bold"), bg="lightgreen", fg="black", borderwidth=5,relief=("sunken"))
    l3.pack()
    l3.config(text=name)

    l2 = Label(root, text=(), font=("mincho", "40", "bold"), bg="black", fg="red", borderwidth=6, relief=("sunken"))
    l2.pack(pady=23)
    lol()


    root.mainloop()


else:
    print("wrong password ")

#+@
