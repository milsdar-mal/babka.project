from tkinter import ttk
import tkinter as tk
from tkinter import *
import sqlite3
def set_data(instrument_id, name, manufacturer, aclass, picture, cost, in_the_store, in_the_warehouse):
    con1 = sqlite3.connect("database.db")
    cur1 = con1.cursor()
    aboba = """
    INSERT INTO instruments
    ([instument id], [name], [manufacturer], [class], [picture], [cost], [in the store], [in the warehouse])
    VALUES (?, ?, ?, ?, ?, ?, ?, ?);
    """
    data = (instrument_id, name, manufacturer, aclass, picture, cost, in_the_store, in_the_warehouse)
    cur1.execute(aboba,data)
    con1.commit()
    con1.close()

def View():
    con1 = sqlite3.connect("database.db")
    cur1 = con1.cursor()
    cur1.execute("SELECT * FROM instruments")
    rows = cur1.fetchall()
    tree.delete(*tree.get_children())
    for row in rows:
        print(row)
        tree.insert("", tk.END, values=row)
    con1.close()

def Rebuild_row():
    window2 = tk.Tk()
    window2.title("Изменение лота")
    l1 = Label(window2, text="первое поле")
    l1.grid(column=0, row=0)

# set_data(2,"гитара","бобровский мебельный завод","струнные","-","10000","да","да")
# set_data(3,"балалайка","бобровский мебельный завод","струнные","-","5000","да","да")
# set_data(4,"кларнет из козьего гузна","новиград","духовае","-","10000000","нет","нет")

window1 = tk.Tk()
window1.title("Продажа")
tree = ttk.Treeview(window1, column=("c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8"), show='headings')
tree.column("#1", anchor=tk.CENTER)
tree.heading("#1", text="instrument id")
tree.column("#2", anchor=tk.CENTER)
tree.heading("#2", text="name")
tree.column("#3", anchor=tk.CENTER)
tree.heading("#3", text="manufacturer")
tree.column("#4", anchor=tk.CENTER)
tree.heading("#4", text="class")
tree.column("#5", anchor=tk.CENTER)
tree.heading("#5", text="picture")
tree.column("#6", anchor=tk.CENTER)
tree.heading("#6", text="cost")
tree.column("#7", anchor=tk.CENTER)
tree.heading("#7", text="in the store")
tree.column("#8", anchor=tk.CENTER)
tree.heading("#8", text="in the warehouse")
tree.pack()
button1 = tk.Button(text="Display data", command=View)
button1.pack(pady=10)
button2 = tk.Button(text="Refactor data", command=Rebuild_row)
button2.pack(pady=10)
window1.mainloop()