import sqlite3
import tkinter

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE sales(
[sale id] INT PRIMARY KEY,
[instrument] INT,
[customer] INT,
[client] INT,
[date] TEXT
)
""")
conn.commit()