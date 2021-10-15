"""
Waahoos: Alejandro Alonso, Ivan Mijacika, William Chen
SoftDev
K14 -- Form and Function
2021-10-14
"""

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object

@app.route("/") #, methods=['GET', 'POST'])
def disp_loginpage():
    return render_template( 'login.html' )


@app.route("/auth") # , methods=['GET', 'POST'])
def authenticate():
    username = request.args['username']
    return render_template( 'response.html', username = request.args['username'], rMethod = request.method )   #response to a form submission



if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
