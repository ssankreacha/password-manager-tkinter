from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle

# TODO Generate Password


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]     # each of these can be changed
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters
    shuffle(password_list)
    final_password = "".join(password_list)
    password_entry.insert(0, final_password)    # inserts final_password into the field


# TODO Save Password
DETAILS = {}


def save():
    # Get entries for each field & append to dictionary
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    DETAILS["Website"] = f"{website}"
    DETAILS["Email"] = f"{email}"
    DETAILS["Password"] = f"{password}\n"

    if website and password or website or password!= "":
        show_info = messagebox.askokcancel(title=website, message=f"These are the details you entered: "
                f"\nEmail: {email} "
                f"\nPassword: {password} "
                f"\nAre you sure you want to save? ")

        if show_info == True:
            with open("Account Details.txt", 'a') as my_new_file:
                for key, value in DETAILS.items():
                    my_new_file.write('%s: %s\n' % (key, value))
                    # Containing characters in fields after add_button pressed & details saved, get cleared
                    website_entry.delete(0, 'end')
                    password_entry.delete(0, 'end')

    elif website or password == "":
        messagebox.showinfo(title="Information!", message="Please don't leave fields empty")


# TODO GUI Setup

# Window
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=40)

# Logo & Canvas
canvas = Canvas(width=290, height=200, highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)


# Labels Website, Email/Username, Password
website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)

email_username_label = Label(text="Email/Username: ")
email_username_label.grid(row=2, column=0)

password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)


# Entries Website, Email/Username, Password
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()   # cursor is focussed on the website_entry

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(index=0, string="example@gmail.com")

password_entry = Entry(width=35)
password_entry.grid(row=3, column=1, columnspan=2)


# Buttons Generate Password, Add
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.place(x=240, y=270)

add_button = Button(width=13, text="Add", command=save)
add_button.place(x=136, y=270)


canvas.mainloop()
