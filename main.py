from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/submit", methods=['POST'])
def submit():
    form = request.form
    username = form['username']
    password = form['password']
    vpass = form['vpass']
    email = form['email']

    username_errors = [
        lenUsername(username),
        spaceUsername(username)
    ]

    password_errors = [
        lenPassword(password),
        spacePassword(password)
    ]

    verify_password_errors = [
        matchPassword(password, vpass)
    ]

    email_errors = [
        countSymbols(email)
    ]

    username_error = None
    for error in username_errors:
        username_error = error
        if error:
            break

    password_error = None
    for error in password_errors:
        password_error = error
        if error:
            break

    email_error = None
    for error in email_errors:
        email_error = error
        if error:
            break

    verify_password_error = None
    for error in verify_password_errors:
        verify_password_error = error
        if error:
            break

    if username_error or password_error or email_error or verify_password_error:
        return render_template("index.html", 
            username_error = username_error,
            password_error = password_error,
            verify_password_error = verify_password_error,
            email_error = email_error,
            username = username,
            email = email)
    return redirect("/welcome?username=" + cgi.escape(username, quote=True))

def lenUsername(username):
    if len(username)>2 and len(username) < 21:
        return None
    return "Please type in a username between 3 and 20 characters."

def lenPassword(password):
    if len(password)>2 and len(password) < 21:
        return None
    return "Please type in a password between 3 and 20 characters."

def matchPassword(password, vpass):
    if len(vpass) < 1:
        return "You must verify your password."
    elif password == vpass:
        return None
    return "Your passwords do not match."

def spaceUsername(username):
    space = " "
    if space not in username:
        return None
    return "You cannot have a space in your username."

def spacePassword(password):
    space = " "
    if space not in password:
        return None
    return "You cannot have a space in your password."

def countSymbols(email):
    required_char = ["@", "."]
    if len(email) == 0:
        return None
    for char in required_char:
        if char not in email:
            return "You must have an '@' symbol and a '.' in your email address."
    return None

# def validEmail():
#     for char in email:
#         if email 


#     if username has space or len(username) < 3:
#         return form with comments

#     if password != vpass:
#         return form with comments

#     if email contains 1 @:
#         return None

#     elif email contains 1 .:
#         return None

#     elif email does not contain " ":
#         return None

#     elif len(email)>3 and len(email)<20:
#         return None

@app.route("/welcome")
def welcome():
    username = request.args.get("username")
    return render_template("welcome.html", username = username)


@app.route("/")
def index():
    return render_template("index.html")



app.run()