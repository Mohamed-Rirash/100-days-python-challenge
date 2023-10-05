from tkinter import *

window = Tk()
window.title("test")
window.minsize(width=500,height=300)


def clicked():
    lable1.config(text=textbox.get())
    

lable1 = Label(text="Test lable",font=("arial",24))
lable1.grid(column=0,row=0)



button1 = Button(text="change label",cursor="hand2", command=clicked)
button1.grid(column=1,row=1)

button1 = Button(text="change label",cursor="hand2", command=clicked)
button1.grid(column=3,row=0)

textbox = Entry(width=10)
textbox.grid(column=3,row=2)



window.mainloop()

