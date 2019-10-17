from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
import mysql.connector
app = Flask(__name__)
@app.route('/home',methods=['GET','POST'])
def home():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        return redirect(url_for('commit'))
@app.route('/commit',methods=['GET','POST'])
def commit():
    if request.method == 'GET':
        return render_template('commit.html')
    else:
        return redirect(url_for('greet'))

@app.route('/hello')
def greet():
    return 'hello world!'

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
@app.route('/',methods=['GET'])
def write_date():
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="123123",database="test_for_board")
    mycu = mydb.cursor()
    sql = "insert into text (name,context) values (%s,%s)"
    val = ('tankie','Hello,your guy from web!')
    mycu.execute(sql,val)
    mydb.commit()
    mycu.close()
    mydb.close()
    return 'hello'

if __name__=='__main__':
    app.run()
