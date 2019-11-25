import pyrebase

from flask import Flask, flash, redirect, render_template, \
     request, url_for

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

config = {
    "apiKey": "AIzaSyBKLJM7c8kcXfr8bM-oGnNz78HmkqOSjOU",
    "authDomain": "test-eb2d6.firebaseapp.com",
    "databaseURL": "https://test-eb2d6.firebaseio.com",
    "projectId": "test-eb2d6",
    "storageBucket": "test-eb2d6.appspot.com",
    "messagingSenderId": "159613523605",
    "appId": "1:159613523605:web:e1b1a58b82790ab583ed9c",
    "measurementId": "G-PE8MPVV9DH"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()
auth = firebase.auth()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/landing/<username>')
def landingPage():
    return render_template('landing.html', username=username)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    unsuccessful = 'Please check your credentials'
    
    if request.method == 'POST':
        email = request.form['username']
        password = request.form['password']
        
        try:
             auth.sign_in_with_email_and_password(email, password)
             return render_template('landing.html', username=email)
        except:
             return render_template('login.html', us=unsuccessful)

    return render_template('login.html', error=error)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = None
    mesg = 'Please enter your credentials'
    unsuccessful = 'Username Exist, or password must be 6 characters'
    
    if request.method == 'POST':
        email = request.form['username']
        password = request.form['password']
        
        try:
             user = auth.create_user_with_email_and_password(email, password)
             return render_template('landing.html', username=email)
        except:
             return render_template('signup.html', us=unsuccessful)

    return render_template('signup.html', error=error)

    
if __name__ == '__main__':
      app.run()