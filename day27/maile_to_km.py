from tkinter import *

def convert():
    miles = input.get()
    km = float(miles) *1.609
    label3.config(text=round(km))

root = Tk()
root.title("mile to km convertor")
root.config(bg="white",padx=105,pady=105)

# widgets
# entery  Label
# Label  Label Label
#         Button
input = Entry(width=10)
input.grid(column=1,row=0)

label1 = Label(text="Mile",font=("arial",15),bg="white")
label1.grid(column=2,row=0)

label2 = Label(text="is equalto:",font=("arial",15),bg="white")
label2.grid(column=0,row=1)

label3 = Label(text="0:",font=("arial",15),bg="white")
label3.grid(column=1,row=1)

label4 = Label(text="KM",font=("arial",15),bg="white")
label4.grid(column=2,row=1)

button1 = Button(text="Calculate",font=("arial",15),bg="black",fg="white",command=convert)
button1.grid(column=1,row=2)

root.mainloop()