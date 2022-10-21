from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    password_list += [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(char for char in password_list)
    input_password.insert(0, password)

    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():

    website_entry = input_website.get()
    email_entry = input_email.get()
    password_entry = input_password.get()
    new_data = {
        website_entry: {
            "email": email_entry,
            "password": password_entry,
        }
    }
    if len(website_entry) == 0 or len(email_entry) == 0 or len(password_entry) == 0:
        messagebox.showinfo(title="Empty Field", message="Some fields are empty. ")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
            with open("data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        finally:
            input_website.delete(0, END)
            input_password.delete(0, END)

def find_password():
    website_entry = input_website.get()
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
            messagebox.showinfo(title=f"{website_entry}:", message=f"Email: {data[website_entry]['email']}\n"
                                                          f"Password: {data[website_entry]['password']}")
    except FileNotFoundError:
        messagebox.showinfo(title="Error -.- ", message="No Data File Found")
    except KeyError:
            messagebox.showinfo(title="No Data File Found", message="No details for the website exists")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
pass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_img)
canvas.grid(row=0, column=1)

#b.grid(column=0, row=2, columnspan=2) per riempire piu colonne
website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username: ")
email_label.grid(row=2, column=0)
pass_label = Label(text="Password: ")
pass_label.grid(row=3, column=0)

input_website = Entry(width=21)
input_website.grid(row=1, column=1)
input_website.focus()

input_email = Entry(width=35)
input_email.grid(row=2, column=1, columnspan=2)
input_email.insert(0, "pythontkinter@eheh.com")

input_password = Entry(width=21)
input_password.grid(row=3, column=1)

button_generate = Button(text="Generate Password", command=generate_password)
button_generate.grid(row=3, column=2)

button_add = Button(width=36, text="Add", command=save_password)
button_add.grid(row=4, column=1, columnspan=2)

button_search = Button(text="Search", command=find_password)
button_search.grid(row=1, column=2)



window.mainloop()

