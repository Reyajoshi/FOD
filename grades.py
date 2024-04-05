import pymysql
import tkinter as tk
from tkinter import messagebox

# Create a connection to MySQL
connection = pymysql.connect(host="localhost",
user="root", password="", database="student_management")

# Create a cursor object
cursor = connection.cursor()


# Function to add a new student
def add_student():
    name = entry_name.get()
    maths_grade = entry_maths_grade.get()
    english_grade = entry_english_grade.get()
    computer_grade = entry_computer_grade.get()
    science_grade = entry_science_grade.get()
    history_grade = entry_history_grade.get()

    # Insert student into database
    cursor.execute("INSERT INTO students (name,maths_grade, english_grade, computer_grade, science_grade, history_grade) VALUES (%s, %s, %s, %s, %s, %s)",
                   (name,maths_grade, english_grade, computer_grade, science_grade, history_grade))
    connection.commit()

    messagebox.showinfo("Success", "Student added successfully")

    # Save student information to grades.txt
    with open("grades.txt", "r") as file:
        data = file.read().strip()

    with open("grades.txt", "a") as file:
        if not data:
            file.write("Name\t\tMaths\t\tEnglish\t\tComputer\t\tScience\t\tHistory\n")  # Write headers if file does not exist
        file.write(f"{name}\t\t\t{maths_grade}\t\t\t{english_grade}\t\t\t{computer_grade}\t\t\t{science_grade}\t\t\t{history_grade}\n")

   

# Function to clear all entry fields
def clear_fields():
    entry_name.delete(0, tk.END)
    entry_maths_grade.delete(0, tk.END)
    entry_english_grade.delete(0, tk.END)
    entry_computer_grade.delete(0, tk.END)
    entry_science_grade.delete(0, tk.END)
    entry_history_grade.delete(0, tk.END)


# Function to display all students
def show_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    # Display students in a message box
    message = "Students:\n"
    for student in students:
        message += f"ID: {student[0]}, Name: {student[1]}, Maths: {student[2]}, English: {student[3]}, Computer: {student[4]}, Science: {student[5]}, History: {student[6]}\n"
    messagebox.showinfo("Students", message)


# Tkinter GUI
root = tk.Tk()
root.title("Student Management System")

# Labels
tk.Label(root, text="Name:").grid(row=0, column=0)
tk.Label(root, text="Maths Grade:").grid(row=1, column=0)  # Maths Grade Label
tk.Label(root, text="English Grade:").grid(row=2, column=0)  # English Grade Label
tk.Label(root, text="Computer Grade:").grid(row=3, column=0)  # Computer Grade Label
tk.Label(root, text="Science Grade:").grid(row=4, column=0)  # Science Grade Label
tk.Label(root, text="History Grade:").grid(row=5, column=0)  # History Grade Label

# Entry fields
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)
entry_maths_grade = tk.Entry(root)  # Entry field for Maths Grade
entry_maths_grade.grid(row=1, column=1)
entry_english_grade = tk.Entry(root)  # Entry field for English Grade
entry_english_grade.grid(row=2, column=1)
entry_computer_grade = tk.Entry(root)  # Entry field for Computer Grade
entry_computer_grade.grid(row=3, column=1)
entry_science_grade = tk.Entry(root)  # Entry field for Science Grade
entry_science_grade.grid(row=4, column=1)
entry_history_grade = tk.Entry(root)  # Entry field for History Grade
entry_history_grade.grid(row=5, column=1)

# Buttons
tk.Button(root, text="Add Student", command=add_student).grid(row=7, column=0, columnspan=2, pady=10)
tk.Button(root, text="Show Students", command=show_students).grid(row=8, column=0, columnspan=2, pady=10)
tk.Button(root, text="Clear Fields", command=clear_fields).grid(row=9, column=0, columnspan=2, pady=10)

root.mainloop()
