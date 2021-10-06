"""
Cool Dogs - Ishraq Mahid & Fish, Ivan Mijacika & Bob, and Gavin McGinley & Craig
SoftDev
k10 -- Flask Greatness -- Exploration of Flask framework -- We explored written code to understand flask and created our own code
2021 - 10 - 4
Questions:
Is there a way to make formatting things easier? Current we have to manually put in br tags and what not, but how can we make this formatting easier?
Does the @app.rout("/") specify that the output of hello_world is what should be put in that route?
Comments:
This task seemed relatively easy. We utilized code that was prebuilt and put 1 and 1 together to create 2.
Summary:
We utilized the flask code we explored earlier on to create a website to randomly select an occupation. We also reused code from k06 
to randomly select an occupation.
"""
from flask import Flask
from randomOcc06 import weighted
from randomOcc06 import generateListStr

app = Flask(__name__)  # create instance of class Flask
tnpg = "<h1>Cool Dogs - Ishraq Mahid & Fish, Ivan Mijacika & Bob, and Gavin McGinley & Craig</h1>"

@app.route("/")  # assign fxn to route
def hello_world():
    #This code does similar to what is done in v3, with the exception of dealing with cases where the file is imported somewhere else
    print("the __name__ of this module is... ")
    print(__name__)
    return tnpg + "<h2>" + weighted() + "</h2>" + generateListStr(None)


if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
