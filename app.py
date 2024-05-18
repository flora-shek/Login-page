from flask import Flask, render_template, request
from flask_bcrypt import Bcrypt
from database import connection

app = Flask(__name__)
bcrypt = Bcrypt(app)

@app.route('/')
def index():
  return render_template('signup.html')

@app.route('/login')
def signin():
  return render_template('signin.html')


@app.route('/login/user', methods=['POST'])
def login():
    username = request.form['floatingInput']
    password = request.form['floatingPassword']
    cursor = connection.cursor()
    sql = "SELECT password FROM `user` WHERE `email`=%s "
    result = cursor.execute(sql,(username))
    result_all = cursor.fetchall()
    pw_hash= result_all[0]['password']
    is_valid = bcrypt.check_password_hash(pw_hash, password) 
    if is_valid:
       return render_template('signin.html', output="Login Successful")
    return render_template('signin.html', output="Try again!")

@app.route('/signup/user', methods=['POST'])
def signup():
  username = request.form['floatingInput']
  password = request.form['floatingPassword']
  password1 = request.form['floatingPassword1']
  
  if password == password1 and len(password)>=8:
      pw_hash =  bcrypt.generate_password_hash(password).decode('utf-8') 
      cursor = connection.cursor()
      sql = "insert into user(email,password) values(%s,%s)"
      result = cursor.execute(sql, (username, pw_hash))
      connection.commit()
      return render_template('signup.html', output="Account Created successfully!!")
      
  return render_template('signup.html', output="Please check if passwords match and is atleast 8 characters long")

if __name__=='__main__':
  app.run(host='0.0.0.0',port=8080,debug=True)