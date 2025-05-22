import random
import string
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

# Main Window
root = Tk()
root.geometry("500x400")
root.title("Password Generator")
root.config(bg='lightskyblue')
root.resizable(False, False)

# Password Variable
password = StringVar()

# Heading
title = Label(root, text="🔐 PASSWORD GENERATOR", font=("Arial", 22, "bold"),bg='lightskyblue', fg='midnightblue')
title.pack(pady=20)

# Frame for Input Options
frame = Frame(root, bg='lightskyblue')
frame.pack(pady=10)

# Password Length Label
length_label = Label(frame, text="Password Length:", font=("Ubuntu", 12),bg='lightskyblue', fg='black')
length_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

# Combobox for Length Selection
length_values = [str(i) for i in range(1, 33)]
length_box = Combobox(frame, values=length_values, font=("Ubuntu", 12),state="readonly", width=5)
length_box.current(7)
length_box.grid(row=0, column=1, pady=5)

# Buttons
def on_enter(event):
    generate_button['bg'] = "#333"
    generate_button['fg'] = "white"

def on_leave(event):
    generate_button['bg'] = "#0C0A47"
    generate_button['fg'] = "white"

# Generate Password Function
def generate_password():
    try:
        length = int(length_box.get())
        characters = string.ascii_letters + string.digits + string.punctuation
        generated = ''.join(random.choices(characters, k=length))
        password.set(generated)
    except:
        messagebox.askretrycancel("Error", "Something went wrong. Please try again.")

# Button to Generate Password
generate_button = Button(root, text="Generate Password", font=("Ubuntu", 12),bg="#0C0A47", fg="white", padx=10,
                          pady=5,command=generate_password, cursor="hand2")
generate_button.pack(pady=20)
generate_button.bind("<Enter>", on_enter)
generate_button.bind("<Leave>", on_leave)

# Result Display
result_label = Label(root, text="Generated Password:", font=("Ubuntu", 12),bg='lightskyblue', fg='black')
result_label.pack()

password_entry = Entry(root, textvariable=password, font=("Ubuntu", 14),fg="green", width=30, justify="center", 
                       state="readonly")
password_entry.pack(pady=10)

root.mainloop()
