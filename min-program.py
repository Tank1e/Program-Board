from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
import mysql.connector

app = Flask(__name__)


#这是主界面，对应的静态文件为home.html
@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'GET':
        database = fetch_data()
        return render_template('home.html',**locals())
    else:
        return redirect('http://122.51.48.86/commit')
        #return redirect('commit')
#这是提交页面，由‘/’主界面post跳转
@app.route('/commit',methods=['GET','POST'])
def commit():
    if request.method == 'GET':
        return render_template('commit.html')
    else:
        #return redirect(url_for('greet'))
        write_data()
        #print_data()
        return redirect('http://122.51.48.86')
        #return redirect(url_for('/'))


#这是一个测试页面
@app.route('/hello')
def greet():
    return 'hello world!'


#这是一个测试页面
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
#@app.route('/',methods=['GET','POST'])

#def write_date():
#    mydb = mysql.connector.connect(host="localhost",user="root",passwd="123123",database="test_for_board")
#    mycu = mydb.cursor()
#    sql = "insert into text (name,context) values (%s,%s)"
#    val = ('tankie','Hello,your guy from web!')
#    mycu.execute(sql,val)
#    mydb.commit()
#    mycu.close()
#    mydb.close()
#    return 'hello'

#if request.method == 'POST':
#这是向数据库写入信息的函数数据库信息
#：host="localhost",user="root",passwd="123123",database="test_for_board"
def write_data():              
    print (request.form.get('name'),request.form.get('text'))            
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="123123",database="test_for_board")
    mycu = mydb.cursor()       
    temp_text = {'name':'Hello','text':'hello from test'}
    #sql = "insert into text (name,context) values (%s,%s)" % (temp_text['name'],temp_text['text'])
    sql = "insert into text (name,context) values (%s,%s)"
    val = (request.form.get('name'),request.form.get('text'))
    #val = ('localtest','localtest')
    mycu.execute(sql,val)
    mydb.commit()
    #print('done')
    mycu.close()
    mydb.close()
#打印信息函数
def fetch_data():
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="123123",database="test_for_board")
    mycu = mydb.cursor()
    mycu.execute("select * from text")
    p=mycu.fetchall()
    #for tip in p:
    #    print(tip) 服务器端打印测试
    return p

if __name__=='__main__':
    app.run()
