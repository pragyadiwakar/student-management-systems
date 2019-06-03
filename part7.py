import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from tkinter import Button



connection = sqlite3.connect('STUDENT_MANAGEMENT.db')

# creating a database

TABLE_NAME = "student_table"
STUDENT_ID = "student_id"
STUDENT_NAME = "student_name"
STUDENT_COLLEGE = "student_college"
STUDENT_ADDRESS = "student_address"
STUDENT_PHONE = "student_phone"

connection.execute(" CREATE TABLE IF NOT EXISTS " + TABLE_NAME + " ( " + STUDENT_ID +
                   " INTEGER PRIMARY KEY AUTOINCREMENT, " + STUDENT_NAME + " TEXT, " + STUDENT_COLLEGE + " TEXT, " +
                   STUDENT_ADDRESS + " TEXT, " + STUDENT_PHONE + " INTEGER);")
print("table created successfully")
mainWindow = tk.Tk()
mainWindow.title("student management system")

name0_Label = tk.Label(mainWindow, text="STUDENT MANAGEMENT SYSTEM", padx=(10), pady=(30))
name0_Label.pack()

name_label = tk.Label(mainWindow, text="enter student name", pady=(10), padx=(20))

name_label.pack()
name1_field = tk.Entry(mainWindow)

name1_field.pack()

college_label = tk.Label(mainWindow, text="enter student college", pady=(10), padx=(20))
college_label.pack()
name2_field = tk.Entry(mainWindow)

name2_field.pack()

address_label = tk.Label(mainWindow, text="enter student address", pady=(10), padx=(20))
address_label.pack()
name3_field = tk.Entry(mainWindow)

name3_field.pack()

phone_label = tk.Label(mainWindow, text="enter student phone", pady=(10), padx=(20))
phone_label.pack()
name4_field = tk.Entry(mainWindow)

name4_field.pack()


def submit():
    name = name1_field.get()
    college = name2_field.get()
    address = name3_field.get()
    phone = name4_field.get()

    connection.execute(
            "INSERT INTO " + TABLE_NAME + " ( " + STUDENT_NAME + ", " + STUDENT_COLLEGE + ", " + STUDENT_ADDRESS
       + ", " + STUDENT_PHONE + ") VALUES ('" + name + "', '" + college + "', " + " '" + address + " ', '" + phone + " '); ")
    connection.commit()
    messagebox.showinfo("Data saved successfully")


def show_records():
    cursor = connection.execute("SELECT * FROM " + TABLE_NAME + " ;")
    for row in cursor:
        print("student id is: ", row[0])
        print("student name is: ", row[1])
        print("student college is: ", row[2])


button = tk.Button(mainWindow, text="submit", command=lambda: submit(), pady=(10), padx=(20))
button.pack()
button = tk.Button(mainWindow, text="show records", command=lambda: show_records(), pady=(10), padx=(20))
button.pack()
mainWindow.mainloop()
