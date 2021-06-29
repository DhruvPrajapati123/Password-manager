from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project


def pass_generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # password_list = []

    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))
    # for char in range(nr_symbols):
    #     password_list.append(random.choice(symbols))

    # for char in range(nr_numbers):
    #     password_list.append(random.choice(numbers))

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #     password += char

    passwordd = "".join(password_list)
    input_3.insert(0, passwordd)
    pyperclip.copy(passwordd)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website_data = input_1.get()
    email_data = input_2.get()
    password_data = input_3.get()
    new_data = {
        website_data: {
            "email": email_data,
            "password": password_data
        }
    }

    if website_data == "" or password_data == "":
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website_data, message=f"These details are entered : \nEmail: {email_data}"
                                       f"\nPassword: {password_data} \nIs it ok to save?")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    # reading the old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # Updating old data with new data
                data.update(new_data)
                # print(data)

                # saving the updated data
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                input_1.delete(0, END)
                input_3.delete(0, END)

# ---------------------------- Search ------------------------------- #


def search():

    website_get = input_1.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File found")
    else:
        if website_get in data:
            email_get = data[website_get]["email"]
            password_get = data[website_get]["password"]
            messagebox.showinfo(title=website_get, message=f"Email: {email_get}\n password: {password_get}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website_get} exist")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

website = Label(text="Website:")
website.grid(column=0, row=1)

email = Label(text="Email/Username:")
email.grid(column=0, row=2)

password = Label(text="Password:")
password.grid(column=0, row=3)

input_1 = Entry(width=17)
input_1.focus()
input_1.grid(column=1, row=1)

input_2 = Entry(width=35)
input_2.insert(0, "dhruv@gmail.com")
input_2.grid(column=1, row=2, columnspan=2)

input_3 = Entry(width=17)
input_3.grid(column=1, row=3)

button = Button(text="Generate Password", command=pass_generate)
button.grid(column=2, row=3)

add = Button(text="Add", width=29, command=save)
add.grid(column=1, row=4, columnspan=2)

search = Button(text="Search", width=12, command=search)
search.grid(column=2, row=1)

window.mainloop()
