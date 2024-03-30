import tkinter as tk
import subprocess

def login():
    # Placeholder function for login functionality
    # Here you would verify the credentials entered by the user
    # For simplicity, let's assume username and password are hard-coded
    username = username_entry.get()
    password = password_entry.get()
    if username == "admin" and password == "adminpass":
        # Redirect to admin dashboard
        subprocess.Popen(["python", "admin.py"])
        window.destroy()  # Close the current login window
    elif username == "user" and password == "userpass":
        # Placeholder for user dashboard
        print("Logged in as user")
    else:
        # Handle invalid login
        print("Invalid username or password")

window = tk.Tk()
window.title("Login student portal")
window.geometry('340x440')
window.configure(bg="#000d66")

login_label = tk.Label(window, text="Login", fg='#FFFFFF', bg='#808080', font=('Times New Roman', 30))
username_label = tk.Label(window, text="Username", fg='#FFFFFF', bg='#808080', font=('Times New Roman', 16))
username_entry = tk.Entry(window, font=('Times New Roman', 16))
password_label = tk.Label(window, text="Password", fg='#FFFFFF', bg='#808080', font=('Times New Roman', 16))
password_entry = tk.Entry(window, show="*", font=('Times New Roman', 16))
login_button = tk.Button(window, text="Login", bg='#808080', fg='#FFFFFF', font=('Times New Roman', 16), command=login)

login_label.grid(row=0, column=1, columnspan=2, sticky="news", pady=50)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1)
login_button.grid(row=3, column=1, columnspan=2)

window.mainloop()
