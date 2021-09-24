from tkinter import *
import pyttsx3




def data():
    print(f"Person Name = {t1.get()}")
    print(f"age ={t2.get()}")
    print(f"address ={t3.get()}")
    print(f"Class ={t4.get()}")
    print(f"Number ={t5.get()}")
    print(f"agree our terms and condition {f1.get()}")

    with open("student.txt","a") as f:
        f.write(f"{t1.get(),t2.get(),t3.get(),t4.get(),t5.get(),f1.get()}\n")

        print("submit {^_^}")
        h = pyttsx3.init()
        h.say("thanku for submiting your information  ")
        h.runAndWait()


root = Tk()

root.geometry("320x333")
root.title("Ghost Droid")
root.minsize(1300,1500)

l=Label(text="Wellcome",bg="red",font="comicsansms 100 bold",relief=GROOVE,borderwidth=6).grid(row=0,column=160,pady=19,padx=19)

l2=Label(text="Name",bg="orange",relief=RIDGE,font="Helvetica 60 ").grid(row=1,column=3,padx=2,pady=5)
l3=Label(text="age",bg="orange",relief=RIDGE,font="Helvetica 60 ").grid(row=2,column=3,padx=2,pady=5)
l4=Label(text="address",bg="orange",relief=RIDGE,font="Helvetica 60 ").grid(row=3,column=3,padx=2,pady=5)
l5=Label(text="class",bg="orange",relief=RIDGE,font="Helvetica 60 ").grid(row=4,column=3,padx=2,pady=5)
l6=Label(text="Number",bg="orange",relief=RIDGE,font="Helvetica 60 ").grid(row=5,column=3,padx=2,pady=5)


t1=StringVar()
t2=StringVar()
t3=StringVar()
t4=StringVar()
t5=StringVar()
t6=StringVar()
f1=IntVar()

a=Entry(l2,textvariable=t1,font="100").grid(row=1,column=4)
b=Entry(l3,textvariable=t2,font="100").grid(row=2,column=4)
c=Entry(l4,textvariable=t3,font="100").grid(row=3,column=4)
d=Entry(l5,textvariable=t4,font="100").grid(row=4,column=4)
e=Entry(l6,textvariable=t5,font="100").grid(row=5,column=4)


Button(text="submit",bg="gray",font=20,relief=GROOVE,command=data ).grid(row=6,column=4,padx=10,pady=10)
check=Checkbutton(text="agree our terms and conditions ?",variable=f1).grid(row=7,column=4)

root.mainloop()
