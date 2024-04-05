import tkinter as tk
import mysql.connector

class StudentDashboard:
    def __init__(self, root, username):
        self.root = root
        self.username = username

        self.root.title("Student Dashboard")
        self.root.geometry("800x600")

        # Initialize variables to store student data
        self.grades = {}
        self.ecas = {}

        # Load grades and ECAs for the logged-in student
        self.load_student_data()

        # Display grades and ECAs
        self.display_student_data()

    def load_student_data(self):
        # Connect to the MySQL database
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="student_management"
        )
        cursor = conn.cursor()

        # Load grades
        cursor.execute("SELECT maths_grade, english_grade, computer_grade, science_grade, history_grade FROM students WHERE name = %s", (self.username,))
        grades_data = cursor.fetchone()
        if grades_data:
            self.grades = {
                "Maths": grades_data[0],
                "English": grades_data[1],
                "Computer": grades_data[2],
                "Science": grades_data[3],
                "History": grades_data[4]
            }

        # Load ECAs
        cursor.execute("SELECT eca, role FROM activities WHERE student_name = %s", (self.username,))
        eca_data = cursor.fetchall()
        if eca_data:
            self.ecas = {row[0]: row[1] for row in eca_data}

        # Close the connection
        conn.close()

    def display_student_data(self):
        # Display grades
        grades_label = tk.Label(self.root, text="Grades", font=('Times New Roman', 18))
        grades_label.pack()

        grades_text = tk.Text(self.root, height=10, width=60)
        grades_text.pack()
        for subject, grade in self.grades.items():
            grades_text.insert(tk.END, f"{subject}: {grade}\n")

        # Display ECAs
        ecas_label = tk.Label(self.root, text="Extracurricular Activities", font=('Times New Roman', 18))
        ecas_label.pack()

        ecas_text = tk.Text(self.root, height=10, width=60)
        ecas_text.pack()
        for activity, role in self.ecas.items():
            ecas_text.insert(tk.END, f"{activity}: {role}\n")

# Get the username from user input or any other source
username = "Riley"  # Example username, replace it with actual user input

root = tk.Tk()
dashboard = StudentDashboard(root, username)
root.mainloop() 
