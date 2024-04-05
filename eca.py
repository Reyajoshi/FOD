import pymysql
import tkinter as tk
from tkinter import messagebox

# Create a connection to MySQL
connection = pymysql.connect(host="localhost", user="root", password="", database="student_management")

# Create a cursor object
cursor = connection.cursor()

# Function to add a new extracurricular activity
def add_activity():
    eca = entry_activity_name.get()
    role = entry_role.get()
    student_name = entry_student_name.get()

    # Insert activity into database
    cursor.execute("INSERT INTO activities (eca, role, student_name) VALUES (%s, %s, %s)",
                   (eca, role, student_name))
    connection.commit()

    messagebox.showinfo("Success", "Activity added successfully")

    with open("eca.txt", "a") as file:
        file.seek(0, 2)  # Move cursor to the end of the file
        if file.tell() == 0:  # Check if file is empty
            file.write("Activity\t\tRole\t\tStudent\n")  # Write heading if file is empty
        file.write(f"{eca}\t\t{role}\t\t{student_name}\n")

# Function to clear all entry fields
def clear_fields():
    entry_activity_name.delete(0, tk.END)
    entry_role.delete(0, tk.END)
    entry_student_name.delete(0, tk.END)

# Function to display all activities
def show_activities():
    cursor.execute("SELECT * FROM activities")
    activities = cursor.fetchall()

    # Display activities in a message box
    message = "Activities:\n"
    for activity in activities:
        message += f"ID: {activity[0]}, Activity: {activity[1]}, Role: {activity[2]}, Student: {activity[3]}\n"
    messagebox.showinfo("Activities", message)

# Tkinter GUI
root = tk.Tk()
root.title("Extracurricular Activity Management System")

# Labels
tk.Label(root, text="Activity Name:").grid(row=0, column=0)
tk.Label(root, text="Role:").grid(row=1, column=0)
tk.Label(root, text="Student Name:").grid(row=2, column=0)

# Entry fields
entry_activity_name = tk.Entry(root)
entry_activity_name.grid(row=0, column=1)
entry_role = tk.Entry(root)
entry_role.grid(row=1, column=1)
entry_student_name = tk.Entry(root)
entry_student_name.grid(row=2, column=1)

# Buttons
tk.Button(root, text="Add Activity", command=add_activity).grid(row=4, column=0, columnspan=2, pady=10)
tk.Button(root, text="Show Activities", command=show_activities).grid(row=5, column=0, columnspan=2, pady=10)
tk.Button(root, text="Clear Fields", command=clear_fields).grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()
