# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2021

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)   #where will this go?
    return "No hablo queso!"

app.debug = True
app.run()

#The same extra string is still there, but, and the rest looks similar
#Right before it runs "app.debug = True" is stated
#It usually says that the debuger is off, so maybe app.debug = True turns it on?

#RESULTS

#Everything went the same as v2 but the debugger is now on!
