#Add your email in line 123

from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- SEARCH WEBSITE ------------------------------- #
def search_website():
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
            if website_input.get().lower() in data:
                website_data = data[website_input.get().lower()]
                email = "email"
                password = "password"
                messagebox.showinfo(title="Website Details",
                                    message=(f"Your email is: {website_data[email]}\n"
                                             f"Your password is : {website_data[password]}"))
            else:
                messagebox.showerror(title="No website found",
                                     message="There was no website that matches this description")
    except FileNotFoundError:
        messagebox.showerror(title="No Passwords Saved", message="You have not saved any website passwords yet.")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():

    password_input.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    pass_letter = [random.choice(letters) for char in range(nr_letters)]
    pass_symbols = [random.choice(symbols) for char in range(nr_symbols)]
    pass_numbers = [random.choice(numbers) for char in range(nr_numbers)]

    password_list = pass_letter + pass_symbols + pass_numbers
    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get().lower()
    email = email_input.get()
    password = password_input.get()
    add_details = False

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if website == "" or email == "" or password == "":
        messagebox.showerror(title="Empty Values", message="There is an empty value. ")
    else:
        add_details = messagebox.askokcancel(title=website,
                                             message=f"These are the details entered: \n Email: {email}\n"
                                                     f"Password: {password}"
                                                     f"\n Is it okay to save?")

    if add_details:
        try:
            with open("data.json", mode="r") as data_file:
                # Reading old data
                data = json.load(data_file)
                #Updating old data with new data
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)        # Adds new_data at the top
        else:
            with open("data.json", mode="w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            email_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.minsize(width=200, height=200)
window.config(padx=20, pady=30, bg="#fff")

lock_logo = Canvas(width=200, height=200, bg="#fff", highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
lock_logo.create_image(120, 100, image=lock_image)
lock_logo.grid(row=0, column=1)

####### Website ########

website_label = Label(text="Website:", bg="#fff")
website_label.grid(row=1, column=0)

website_input = Entry(width=30)
website_input.grid(row=1, column=1, sticky="w")
website_input.focus()

####### Email ########

email_label = Label(text="Email/Username:", bg="#fff")
email_label.grid(row=2, column=0)

email_input = Entry(width=52)
email_input.insert(index=0, string="abc@email.com")
email_input.grid(row=2, column=1,columnspan=2, sticky="w",pady=10)

####### Password ########

password_label = Label(text="Password:", bg="#fff")
password_label.grid(row=3, column=0)

password_input = Entry(width=30)
password_input.grid(row=3, column=1, sticky="w",pady=10)

generate_password_button = Button(width=15,text="Generate Password", bg="#fff",command=generate_password)
generate_password_button.grid(row=3, column=2)

####### Add Button ########

add_button = Button(width=44, text="Add", bg="#fff", command=save)
add_button.grid(row=4, column=1, columnspan=2)

####### Search Button ########

search_button = Button(width=15,text="Search",bg="#fff",command=search_website)
search_button.grid(row=1, column=2, sticky="w")

window.mainloop()