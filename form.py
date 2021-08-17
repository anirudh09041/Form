from tkinter import *
import sqlite3
with sqlite3.connect("formdb.db") as db:
    cursor = db.cursor()
    
cursor.execute("""CREATE TABLE IF NOT EXISTS student(name text NOT NULL,department text NOT NULL);""")


def add_new_entry():
    newStud = nm.get()
    newDep = dt.get()
    cursor.execute("insert into student(name,department) values(?,?)",(newStud,newDep))
    db.commit()
                    

root = Tk()
root.title("FORM")
root.geometry('400x400')

name = Label(root,text="NAME:",bg='lightgreen')
dep = Label(root,text="DEPARTMENT:",bg='lightgreen')
name.grid(row=0,column=0,sticky=W,pady=2)
dep.grid(row=1,column=0,sticky=W,pady=2)

nm = Entry(root,text="")
dt = Entry(root,text="")

nm.grid(row=0,column=1,pady=2)
dt.grid(row=1,column=1,pady=2)

button = Button(text="Add", command= add_new_entry)
button.grid(row=3,column=2,sticky=E)

root.mainloop()
