from flask import Flask, request, render_template
import re

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/")
def index():
    
    return render_template('homepage.html')




@app.route("/", methods=['POST'])
def validate_data():
    username = request.form['username']
    password = request.form['password']
    vpassword = request.form['vpassword']
    email = request.form['email']
    usererror=''
    emailerror=''
    passworderror=''
    vpassworderror=''
    error=False
    

    
    if not username or username.strip() == "" or len(username)>20 or len(username)<3:
        usererror = "Please type a username without spaces and with more than 2 and less than 21 characters"
        error=True
    if (not password) or (password.strip() == "") or len(password)>20 or len(password)<3:
        passworderror = "Please type a password without spaces and with more than 2 and less than 21 characters"
        error=True


    # if the user typed nothing at all, redirect and tell them the error
    if (not vpassword) or (vpassword.strip() == "") or vpassword != password:
        vpassworderror = "Please type your password"
        error=True

    # if the user typed nothing at all, redirect and tell them the error
    if len(email)>20 or len(email)<3:
        emailerror = "Please type a valid email address"
        error=True

    # if the user doesn't meet password requirement, redirect and tell them the error
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        emailerror = "Please type a valid email address"
        error=True
            
    if error:        
        return render_template('homepage.html', usererror=usererror, passworderror=passworderror, 
        vpassworderror=vpassworderror, emailerror=emailerror, username=username, password=password, vpassword=vpassword, email=email)  
     # if we didn't redirect by now, then all is well
    else:
        return render_template('welcome.html', username=username)

app.run()

