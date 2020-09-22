import sqlite3


con = sqlite3.connect("weather.db")
print("Database created Successfully")

con.execute("create table city (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL)")
print("Connection created Successfully")

con.close()