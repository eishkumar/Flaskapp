from flask import Flask
from flask import render_template
from flask import request
import models 
from models import *

app = Flask(__name__)
@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method=='POST':
        username = request.form['username']
        fname = request.form['fname']
        name = request.form['name']
        password = request.form['password']
        insertUser(fname,name,username,password)
        users = retrieveUsers1()
        return render_template('res.html',users=users)
    else:  
    	return render_template('index1.html')  
       # users1= dbHandler.delete_all_tasks()
@app.route('/del', methods=['POST','GET'])
def delete():
	if request.method=='POST':
		username = request.form.args['username']
		delete_all_tasks(username)
        # password = request.form['password']e
    #     users1= delete_all_tasks()
		users = retrieveUsers1()

		return render_template('res.html',users=users)
	else:
		return render_template('res2.html')
    # else:

    #     return render_template('index1.html')
    # if not session.get('Log In'):
    #     abort(401)
    # if request.method == 'POST' and form.validate_on_submit():
        
        # db.execute('delete from entries where id=' +)

        
  
    
    # else #request.method == 'GET':
	#return render_template('res.html')

        #return render_template('res.html',users=users1)
   	# elif request.method=='GET':
   	# 	username = request.form.get['username']
   	# 	password = request.form.get['password']
   	# 	dbHandler.del3()
   	# 	users = dbHandler.del3()
   	# 	return render_template('res.html',users=users)
# def main():
#     database = "database2.db"
 
#     # create a database connection
#     conn = create_connection(database)
#     with conn:
#         delete_task(conn, 2);
    # else:	
    #     return render_template('index1.html')
# @app.route('/handle_data', methods=['POST','GET'])
# def handle_data():
#     projectpath = request.form['projectFilepath']
#     return render_template('res2.html')


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')




































































