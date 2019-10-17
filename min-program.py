from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
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
    


if __name__=='__main__':
    app.run()
