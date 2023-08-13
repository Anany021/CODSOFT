import tkinter as tk
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_and_display_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            password_label.config(text="Please enter a positive integer.")
        else:
            password = generate_password(length)
            password_label.config(text="Generated Password:\n" + password)
    except ValueError:
        password_label.config(text="Invalid input. Please enter a positive integer.")

# Create the main window
root = tk.Tk()
root.title("Password Generator App")

# Create and place widgets
length_label = tk.Label(root, text="Enter desired password length:",bg="dark blue",fg="yellow")
length_label.pack(pady=10)

length_entry = tk.Entry(root)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_and_display_password,bg="Dark blue",fg="yellow")
generate_button.pack(pady=10)

password_label = tk.Label(root, text="",bg="Dark blue",fg="yellow")
password_label.pack()
root.configure(bg="Dark blue")
# Start the GUI event loop
root.mainloop()

