from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    #Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char
    password_input.delete(0,END)
    password_input.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():

    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("day30/data.json", "r") as file:
                #Reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open("day30/data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)

            with open("day30/data.json", "w") as file:
                #Saving updated data
                json.dump(data, file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_input.get()
    try:
        with open("day30/data.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")







# ---------------------------- UI SETUP ------------------------------- #


root = Tk()
root.title("Password Manager")
root.config(background="white", padx=20, pady=20)

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
lock_image = PhotoImage(file="day29/logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", bg="white", font=("arial", 13, "bold"))
website_label.grid(column=0, row=1, sticky="w")  

website_input = Entry(width=23, bd=1,highlightcolor="light blue")
website_input.grid(column=1, row=1, columnspan=2, sticky="w")  
website_input.focus()

email_label = Label(text="Email/UserName:", bg="white", font=("arial", 13, "bold"))
email_label.grid(column=0, row=2, sticky="w")  

email_input = Entry(width=35, bd=1,highlightcolor="light blue")
email_input.grid(column=1, row=2, columnspan=2, sticky="w")
email_input.insert(0,"rirash@rirash.com")

password_label = Label(text="Password:", bg="white", font=("arial", 13, "bold"))
password_label.grid(column=0, row=3, sticky="w")  

password_input = Entry(width=21, bd=1,highlightcolor="light blue")
password_input.grid(column=1, row=3, sticky="w")  

password_generator = Button(text="Generate Password", bg="white", width=14, bd=1,highlightcolor="light blue",command=generate_password)
password_generator.grid(column=2, row=3)


search_button = Button(text="search", bg="white", width=14, bd=1,highlightcolor="light blue",command=find_password)
search_button.grid(column=2, row=1)

save_button = Button(text="Save Password", bg="white", width=36, bd=1,highlightcolor="light blue",command=save_data)
save_button.grid(column=1, row=4, columnspan=2, sticky="w")  

root.mainloop()