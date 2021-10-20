"""
Waahoos: Alejandro Alonso, Ivan Mijacika, William Chen
SoftDev
K15 -- Sessions Greetings
2021-10-20
"""

from flask import Flask, render_template, request, session, redirect, url_for    #facilitate form submission
#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object

user = "waahoos"
pwd = "aaimwc"

app.secret_key = "k15"

@app.route("/", methods=['GET', 'POST']) #, methods=['GET', 'POST'])
def index():
    """
    create the basic login page, if session active auto-sign in
    """
    if 'username' in session:
        return render_template('response.html', username=user)
    return render_template('login.html')

@app.route("/auth", methods=['GET', 'POST']) # , methods=['GET', 'POST'])
def auth():
    """
    generate and fill out the response page using flask vars, check validity of inputs
    """
    if app.debug:
        print("\n\n\n")
        print("***DIAG: this Flask obj ***")
        print(app)
        print("***DIAG: request obj ***")
        print(request)
        print("***DIAG: request.args ***")
        print(request.args)
        print("***DIAG: session***")
        print(session)

    try:
        if user==request.args.get("username"):
            if pwd==request.args.get("password"):
                session['username'] = user
                return render_template('response.html', username=user)  #response to a correct form submission
            else:
                return render_template('error.html', error_message="Incorrect Password.")  #response to an incorrect password submission
        else:
            return render_template('error.html', error_message="Username not found.")  #response to an incorrect username submission
    except:
        return render_template('error.html', error_message="Invalid submission.")  #response to a broken submission

@app.route("/logout", methods=["GET", "POST"])
def logout():
    """
    logout method, redirects to login page
    """
    session.pop("username", default=None)
    return redirect(url_for('index'))

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
