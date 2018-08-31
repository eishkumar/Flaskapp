import flask
import os
#PEOPLE_FOLDER=os.path.join('static','people_photo')

from flask import Flask
from flask import render_template,request,url_for
from wtforms import Form, BooleanField, StringField, PasswordField, validators

app = Flask(__name__,static_url_path="")



class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.email.data,
                    form.password.data)
        db_session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)
@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)
# @app.route('/hello')
# def lionel(): 
#     return app.send_static_file('inde.html')   
# @app.route('/eish')
# def elcome():
# 	return render_template('ht.html')

if __name__ == '__main__':
    app.run(host='localhost',port=8000)    