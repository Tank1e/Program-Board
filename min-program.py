from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/hello')
def greet():
    return'hello world!'

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
#def do_the_login_form()
    

if __name__=='__main__':
    app.run()
