import flask
from flask import Flask
from flaskext.mysql import MySQL
from flask import render_template,request
# import db
# app=Flask(__name__)
app = Flask(__name__)
# db=db.load(open('db'))
# app.config['MYSQL_HOST']=db['mysql_host']
# app.config['MYSQL_USER']=db['mysql_user']
# app.config['MYSQL_PASSWORD']=db['mysql_password']
# app.config['MYSQL_DB']=db['mysql_db']
# mysql=MYSQL(app)
@app.route('/')
def hello():
	if request.method=='POST':
		userdetails=request.form
		name=userdetails['name']
		email=userdetails['email']
	# 	cur=mysql.connection.cursor()
	# 	cur.execute("INSERT INTO users(name,email)values(%s,%s)",(name,email))
	# 	mysql.connection.commit()
	# 	cur.close()
	# 	return 'success'

		return render_template('register1.html')
	else:
		return render_template('form1.html')
@app.route('/welcome')
def welcome():
	return render_template('two.html')
@app.route('/log')	
def name():
	return render_template('thr.html')
		

if __name__=="__main__":
	app.run(host='localhost',port=8000)