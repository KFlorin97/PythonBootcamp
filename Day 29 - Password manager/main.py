from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = websiteEntry.get()
    email = emailEntry.get()
    password = passwordEntry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title = "Take care", message = "Please make sure you completed all the fields")
    else:
        isOk = messagebox.askokcancel(title = website, message = f"There are the details you entered: \nEmail :{email}\n"
                               f"Password: :{password}\nIs it ok to save?")

        if isOk:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                websiteEntry.delete(0, END)
                passwordEntry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password manager")
window.config(padx = 50, pady = 50)

#Canvas
canvas = Canvas(height = 200, width = 200)
logo_img = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image = logo_img)
canvas.grid(row = 0, column = 1)

#Labels
websiteLabel = Label(text = "Website")
websiteLabel.grid(row = 1, column = 0)
emailLabel = Label(text = "Email/Username")
emailLabel.grid(row = 2, column = 0)
passwordLabel = Label(text = "Password")
passwordLabel.grid(row = 3, column = 0)

#Entries
websiteEntry = Entry(width = 35)
websiteEntry.grid(row = 1, column = 1, columnspan = 2)
websiteEntry.focus()
emailEntry = Entry(width = 35)
emailEntry.grid(row = 2, column = 1, columnspan = 2)
emailEntry.insert(0, "testingcode@gmail.com")
passwordEntry = Entry(width = 21)
passwordEntry.grid(row = 3, column = 1)

#Buttons
addButton = Button(text = "Add", width = 36, command = save)
addButton.grid(row = 4, column = 1, columnspan = 2)


window.mainloop()