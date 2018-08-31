import sqlite3
from sqlite3 import *
connection=connect("database2.db")
connection.execute('''CREATE TABLE users6(fname char(20),name char(20),Username char(20),Password varchar(20))''')
connection.close()
