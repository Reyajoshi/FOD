from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox
import random




class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")

        title=Label(self.root,text="Student Management System",bd=10,relief=GROOVE,font=("times new roman",30,"bold"),bg="#000d66",fg="white")
        title.pack(side=TOP,fill=X)

        ##all variables
        self.Roll_No_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()

        self.search_by=StringVar()
        self.search_txt=StringVar()

        # manage frame
        Manage_frame=Frame(self.root,bd=4,relief=RIDGE,bg="#add8e6")
        Manage_frame.place(x=20,y=100,width=450,height=600)

        m_title=Label(Manage_frame,text="Manage Students",font=("times new roman",25,"bold"),bg="#add8e6",fg="#000d66")
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_roll=Label(Manage_frame,text="Roll no:",font=("times new roman",20,"bold"),bg="#add8e6",fg="#000d66")
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")


        txt_Roll=Entry(Manage_frame,textvariable=self.Roll_No_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")


        lbl_name=Label(Manage_frame,text="Name:",font=("times new roman",20,"bold"),bg="#add8e6",fg="#000d66")
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")


        txt_Name=Entry(Manage_frame,textvariable=self.name_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Name.grid(row=2,column=1,pady=10,padx=20,sticky="w")
        
        lbl_Email=Label(Manage_frame,text="Email:",font=("times new roman",20,"bold"),bg="#add8e6",fg="#000d66")
        lbl_Email.grid(row=3,column=0,pady=10,padx=20,sticky="w")


        txt_Email=Entry(Manage_frame,textvariable=self.email_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Email.grid(row=3,column=1,pady=10,padx=20,sticky="w")

        lbl_Gender=Label(Manage_frame,text="Gender:",font=("times new roman",20,"bold"),bg="#add8e6",fg="#000d66")
        lbl_Gender.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        combo_gender=ttk.Combobox(Manage_frame,textvariable=self.gender_var,font=("times new roman",13,"bold"),state='readonly')
        combo_gender['values']=("male","female","others")
        combo_gender.grid(row=4,column=1,padx=20,pady=10)


        lbl_Contact=Label(Manage_frame,text="Contact:",font=("times new roman",20,"bold"),bg="#add8e6",fg="#000d66")
        lbl_Contact.grid(row=5,column=0,pady=10,padx=20,sticky="w")


        txt_Contact=Entry(Manage_frame,textvariable=self.contact_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Contact.grid(row=5,column=1,pady=10,padx=20,sticky="w")

        lbl_DOB=Label(Manage_frame,text="D.O.B:",font=("times new roman",20,"bold"),bg="#add8e6",fg="#000d66")
        lbl_DOB.grid(row=6,column=0,pady=10,padx=20,sticky="w")


        txt_DOB=Entry(Manage_frame,textvariable=self.dob_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_DOB.grid(row=6,column=1,pady=10,padx=20,sticky="w")

        lbl_Address=Label(Manage_frame,text="Address:",font=("times new roman",20,"bold"),bg="#add8e6",fg="#000d66")
        lbl_Address.grid(row=7,column=0,pady=10,padx=20,sticky="w")

        self.txt_Address=Text(Manage_frame,width=30,height=3,font=("",10))
        self.txt_Address.grid(row=7,column=1,pady=10,padx=20,sticky="w")

        ##button frame
        button_frame=Frame(Manage_frame,bd=4,relief=RIDGE,bg="#add8e6")
        button_frame.place(x=15,y=500,width=420)

        Addbtn=Button(button_frame,text="Add",width=10,command=self.add_students).grid(row=0,column=0,padx=10,pady=10)
        Updatebtn=Button(button_frame,text="Update",width=10,command=self.update_data).grid(row=0,column=1,padx=10,pady=10)
        Deletebtn=Button(button_frame,text="Delete",width=10,command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
        Clearbtn=Button(button_frame,text="Clear",width=10,command=self.clear).grid(row=0,column=3,padx=10,pady=10)
        save_btn = Button(button_frame, text="Save to Text", command=self.save_to_txt)
        save_btn.grid(row=1, column=1, pady=10)
        password_btn = Button(button_frame, text="Save Password", command=self.save_password_to_txt)
        password_btn.grid(row=1, column=2, pady=10)
        






        #detail frame
        Detail_frame=Frame(self.root,bd=4,relief=RIDGE,bg="#add8e6")
        Detail_frame.place(x=500,y=100,width=800,height=560)

        lbl_search=Label(Detail_frame,text="Search By:",font=("times new roman",20,"bold"),bg="#add8e6",fg="#000d66")
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        combo_search=ttk.Combobox(Detail_frame,textvariable=self.search_by,width=10,font=("times new roman",13,"bold"),state='readonly')
        combo_search['values']=("Roll_no","Name","Contact")
        combo_search.grid(row=0,column=1,padx=20,pady=10)


        txt__Search=Entry(Detail_frame,textvariable=self.search_txt,width=20,font=("times new roman",11,"bold"),bd=5,relief=GROOVE)
        txt__Search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

        searchbtn=Button(Detail_frame,text="Search",width=10,pady=5,command=self.search_data).grid(row=0,column=3,padx=10,pady=10)
        showallbtn=Button(Detail_frame,text="Show all",width=10,pady=5,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)

        #table frame

        Table_frame=Frame(Detail_frame,bd=4,relief=RIDGE,bg="#add8e6")
        Table_frame.place(x=10,y=70,width=760,height=480)

        scroll_x=Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_frame,orient=VERTICAL)

        self.Student_table=ttk.Treeview(Table_frame,columns=("roll","name","email","gender","contact","dob","address"))
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("roll",text="Roll_no")
        self.Student_table.heading("name",text="Name")
        self.Student_table.heading("email",text="Email")
        self.Student_table.heading("gender",text="Gender")
        self.Student_table.heading("contact",text="Contact")
        self.Student_table.heading("dob",text="D.O.B")
        self.Student_table.heading("address",text="Address")
        self.Student_table['show']='headings'
        self.Student_table.column("roll",width=100)
        self.Student_table.column("name",width=100)
        self.Student_table.column("gender",width=100)
        self.Student_table.column("contact",width=100)
        self.Student_table.column("dob",width=100)
        self.Student_table.column("address",width=150)
        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
    
    def save_to_txt(self):
        roll_no = self.Roll_No_var.get()
        name = self.name_var.get()
        email = self.email_var.get()
        gender = self.gender_var.get()
        contact=self.contact_var.get()
        dob=self.dob_var.get()
        address = self.txt_Address.get('1.0', END).strip()

        # Check if the file already contains data
        with open("users.txt", "r") as file:
            data = file.read().strip()

        # Open the text file in append mode
        with open("users.txt", "a") as file:
            # If the file is empty, write the headings first
            if not data:
                file.write("Rollno\t\tName\t\tEmail\t\t\tGender\t\tContact\t\t\tD.O.B\t\t\tAddress\n")

            # Write the student data
            file.write(f"{roll_no}\t\t{name}\t\t{email}\t{gender}\t\t{contact}\t\t{dob}\t{address}\n")
        messagebox.showinfo("Success", "Data saved to users.txt")
    
    def generate_password(self):
        # Generate a 4-digit random password
        password = ''.join(random.choices('0123456789', k=5))
        return password
    
    def save_password_to_txt(self):
        roll_no=self.Roll_No_var.get()
        name = self.name_var.get()
        password = self.generate_password()

        # Check if the file is empty
        with open("password.txt", "r") as file:
            data = file.read().strip()

        # Open the text file in append mode
        with open("password.txt", "a") as file:
            # Write the headings if the file is empty
            if not data:
                file.write("Rollno\t\tName\t\tPassword\n")
            # Write the name and password
            file.write(f"{roll_no}\t\t\t{name}\t\t{password}\n")

        messagebox.showinfo("Success", f"Name and Password saved to password.txt")


    def add_students(self):
        if any([
        self.Roll_No_var.get() == "",
        self.name_var.get() == "",
        self.email_var.get() == "",
        self.gender_var.get() == "",
        self.contact_var.get() == "",
        self.dob_var.get() == "",
        self.txt_Address.get('1.0', END) == ""
        ]):
            messagebox.showerror("Error", "All fields are required!!")
        else:
                con=pymysql.connect(host="localhost",user="root",password="",database="stm")
                cur=con.cursor()
                cur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s)",(
                    self.Roll_No_var.get(),
                    self.name_var.get(),
                    self.email_var.get(),
                    self.gender_var.get(),
                    self.contact_var.get(),
                    self.dob_var.get(),
                    self.txt_Address.get('1.0',END)
                    ))
        
                con.commit()
                self.fetch_data()
                self.clear()
                con.close()
                messagebox.showinfo("Success","Record has been inserted")
    


    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("select * from student")
        rows=cur.fetchall()
        if len(rows)!=0:
                self.Student_table.delete(*self.Student_table.get_children())
                for row in rows:
                        self.Student_table.insert('',END,values=row)
                con.commit()
        con.close()
    
    def clear(self):
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_Address.delete("1.0",END)


    def get_cursor(self,ev):
        cursor_row=self.Student_table.focus()
        contents=self.Student_table.item(cursor_row)
        row=contents['values']
        if len(row) > 0:
            self.Roll_No_var.set(row[0])
            self.name_var.set(row[1])
            self.email_var.set(row[2])
            self.gender_var.set(row[3])
            self.contact_var.set(row[4])
            self.dob_var.set(row[5])
            self.txt_Address.delete("1.0",END)
            self.txt_Address.insert(END,row[6])

    def update_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("UPDATE student SET name=%s, email=%s, gender=%s, contact=%s, `d.o.b`=%s, address=%s WHERE roll_no=%s", (
        self.name_var.get(),
        self.email_var.get(),
        self.gender_var.get(),
        self.contact_var.get(),
        self.dob_var.get(),
        self.txt_Address.get('1.0', END),
        self.Roll_No_var.get()
        ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def delete_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("DELETE FROM student WHERE roll_no=%s", (self.Roll_No_var.get(),))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
    
    def search_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()

        
        cur.execute("SELECT * FROM student WHERE " + str(self.search_by.get()) + " LIKE '%" + str(self.search_txt.get()) + "%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
        for row in rows:
            self.Student_table.insert('', END, values=row)
        con.commit()
        con.close()

root = Tk()
obj = Student(root)
root.mainloop()
