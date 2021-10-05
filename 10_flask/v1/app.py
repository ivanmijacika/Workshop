# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2021

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    return "No hablo queso!"

app.run()

# similar to previous app.py from v0 but it doesn't have a call to print __name__, so it should still say "No hable queso!" on the browser but nothing should be printed in the terminal.

#RESULTS

# As expected it had the same message in the browser but in the terminal it didn't print anything.
# It just skipped the __name__ part, so it probably isn't too important
