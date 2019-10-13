
from tkinter import *
import sqlite3
root = Tk()
root.geometry('500x500')
root.title("harsh")


def insert():
    name = name_field.get()
    phone = phone_field.get()
    add = add_field.get()
    conn = sqlite3.connect("test.db")
    conn.execute(
        '''CREATE TABLE IF NOT EXISTS data (name TEXT,phone TEXT,adderess TEXT)''')
    with conn:
        a = conn.cursor()
        a.execute(
            "Insert into data( name,phone, adderess) VALUES(?,?,?)", (name, phone, add))
        conn.commit()


Label(root, text="Form").grid(row=0, column=1)

name = Label(root, text="first name").grid(row=1, column=0)
phone = Label(root, text="phone").grid(row=2, column=0)
adderess = Label(root, text="adderess").grid(row=3, column=0)
name_data = StringVar()
phone_data = StringVar()
add_data = StringVar()
name_field = Entry(root, textvar=name_data)
course_field = Entry(root, textvar=phone_data)
sem_field = Entry(root, textvar=add_data)
name_field.grid(row=1, column=1, ipadx="100")
course_field.grid(row=2, column=1, ipadx="100")
sem_field.grid(row=3, column=1, ipadx="100")
b1 = Button(root, text="Submit", fg="black", command=insert).grid(column=1)

root.mainloop()
