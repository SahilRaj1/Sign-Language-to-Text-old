from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Sign Language to Text convertor")
root.geometry("700x700")


def myIns():
    messagebox.showinfo(
        "Instructions",
        "1.Place your hand in front of the webcam.\n2.Show the Sign Language number in the square frame.\n3.Please wait till the image is processed.\n4.You will now get the desired output below.",
    )


def myAbout():
    messagebox.showinfo("About", f"Sign Language to text {chr(169)}\nSahil, Saatvik, Anushka, Vithi")


l1 = Label(root, text="SIGN LANGUAGE TO TEXT ", font="arial 24 bold", fg="blue")
l1.place(x=150, y=40)


btn_about = Button(
    padx=3,
    pady=3,
    bd=1,
    fg="white",
    font=("ariel", 10, "bold"),
    text="About",
    bg="black",
    command=myAbout,
)
btn_about.place(y=0, x=650)

btn_ins = Button(
    padx=3,
    pady=3,
    bd=1,
    fg="white",
    font=("ariel", 10, "bold"),
    text="Instruction",
    bg="black",
    command=myIns,
)
btn_ins.place(y=0, x=0)


f1 = Frame(root, bg="white", bd=5, relief=SUNKEN)
f1.place(x=140, y=140, height=300, width=400)


l2 = Label(root, text="CHARACTER   : ", font="arial 20 bold", fg="black")
l2.place(x=50, y=500)

l3 = Label(root, text="NUMBER          : ", font="arial 20 bold", fg="black")
l3.place(x=50, y=550)

l3 = Label(root, text="NO OF DIGITS  : ", font="arial 20 bold", fg="black")
l3.place(x=50, y=600)


root.mainloop()
