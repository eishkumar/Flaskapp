import sqlite3 as sql

def insertUser(fname,name,username,password):
    con = sql.connect("database2.db")
    cur = con.cursor()
    cur.execute("INSERT INTO users6(fname,name,username,password) VALUES (?,?,?,?)", (fname,name,username,password))
    con.commit()
    con.close()

def retrieveUsers():
	con = sql.connect("database2.db")
	cur = con.cursor()
	cur.execute("SELECT fname,name,username,password FROM users6")
	users6 = cur.fetchall()
	con.close()
	return users6

def retrieveUsers1():
	con = sql.connect("database2.db")
	cur = con.cursor()
	cur.execute("SELECT * FROM users6")
	users6 = cur.fetchall()
	con.close()
	return users6	
def delete_all_tasks(username):
	print(username)
	con=sql.connect("database2.db")
	cur=con.cursor()
    # cur.execute("DELETE FROM users6 WHERE password=444")
    # users6 = cur.fetchall()
    # con.close()
	cursor=con.execute("DELETE FROM users6 WHERE password = '%s';"%username.strip())
    #print(next(cursor))
    # cur.execute('delete from users6 where password=' + a )
	cur.execute("SELECT fname,name,username,password FROM users6")
	users6 = cur.fetchall()
	con.commit()
	con.close()
	return users6
    # # cursor = con.execute("SELECT fname,name,username,password from users6")
    # # con.commit()
    # con.close()
#     conn = sqlite3.connect('databaza.db')
# c = conn.cursor()
# conn.text_factory = str    
# data3 = str(input('Please enter name: '))
# query = "DELETE FROM Zoznam WHERE Name = '%s';" % data3.strip()
# print(query)
# mydata = c.execute(query)

       
# def delete_task(conn, username):
#     """
#     Delete a task by task id
#     :param conn:  Connection to the SQLite database
#     :param id: id of the task
#     :return:
#     """
#     sql = 'DELETE FROM users3 WHERE username=?'
#     cur = conn.cursor()
#     cur.execute(sql, (id,))
# def del3():
# 	con = sq.connect('database2.db')
# 	cur = con.cursor()
# 	# con.text_factory = str    
# 	data3 = str(input('Please enter name: '))
# 	query = "DELETE FROM users3 WHERE password= '%s';" % data3.strip()
# 	# print(query)
# 	#mydata = c.execute(query)	
# 	cur.execute("DELETE FROM users3 WHERE Username = '%s';" % data3.strip())
# 	con.commit()
    #con.close()