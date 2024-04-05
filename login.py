import tkinter as tk
import subprocess

def login():
    # Get the entered username and password
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    # Set a flag to indicate whether a valid user has been found
    valid_user_found = False

    # Check if entered credentials match any student's credentials
    with open("password.txt", "r") as password_file:
        for line in password_file:
            data = line.strip().split()
            if len(data) >= 3:
                _, username, password = data
                if entered_username == username and entered_password == password:
                    # Redirect to student dashboard
                    subprocess.Popen(["python", "student_dashboard.py"])
                    window.destroy()  # Close the current login window
                    return
                valid_user_found = True  # Set the flag to True if at least one valid user is found

    # Handle invalid login
    if not valid_user_found:
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
