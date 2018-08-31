import sqlite3
from sqlite3 import *
connection=connect("database1.db")
connection.execute('''CREATE TABLE users(Username char(20),Password varchar(20))''')
connection.close()