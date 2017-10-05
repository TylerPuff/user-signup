from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

tasks = []

@app.route('/')
def index():
   
    return render_template('main.html')

@app.route('/Signup',methods=['POST'])
def Signup():    
    return render_template('Signup.html')
if __name__ == '__main__':

    app.run()