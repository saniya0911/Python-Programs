from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    
    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    
    password = "".join(password_list)
    password_entry.insert(END, password)
    pyperclip.copy(password)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_clicked():
    website = website_entry.get()
    email = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Oops!", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it okay to save ?")
        if is_ok:    
            #reading old data
            try:
                with open("myprog/Projects/PasswordManager/data.json", "r") as f:
                    data = json.load(f)
            except FileNotFoundError:
                with open("myprog/Projects/PasswordManager/data.json", "w") as f:
                    json.dump(new_data, f, indent=4)
            else:
                #Updating old data with new data
                data.update(new_data)
                #Saving new data
                with open("myprog/Projects/PasswordManager/data.json","w") as f:
                    json.dump(data, f, indent=4)
            finally:
                messagebox.showinfo(title="Success", message="Your details were saved.")
                website_entry.delete(0,END)
                password_entry.delete(0,END)

# ---------------------------- Search ------------------------------- #
                
def search_file():
    website = website_entry.get()
    try:
        with open("myprog/Projects/PasswordManager/data.json", "r") as f:
            data = json.load(f)
            email = data[website]["email"]
            password = data[website]["password"]
        messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password}")
    except:
        messagebox.showerror(title="Error", message=f"{website} doesn't exist.")
    finally:
        website_entry.delete(0,END)
        password_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=80, pady=60)

canvas = Canvas(width=200,height=200)
logo = PhotoImage(file="myprog/Projects/PasswordManager/logo.png")
canvas.create_image(100,100,image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)


website_entry = Entry(width=32)
website_entry.grid(row=1, column=1)
website_entry.focus()

username_entry = Entry(width=50)
username_entry.insert(END,"ssaniya.123@gmail.com")
username_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=32)
password_entry.grid(row=3, column=1)

generate_password = Button(text="Generate Password", width=14, command=generate_password)
generate_password.grid(row=3, column=2)

add = Button(text="Add", width=42, command=add_clicked)
add.grid(row=4, column=1, columnspan=2)

search = Button(text="Search", width=14, command=search_file)
search.grid(row=1, column=2)

window.mainloop()