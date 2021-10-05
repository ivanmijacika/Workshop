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

app.run()

#Two print statments instead of one, interesting
#The second print statement is familiar from v0 but the first one adds an extra string before it, maybe it will print right before on the same line.
#The rest looks about the same, so they only thing that should change is the terminal.

#RESULTS

#It did not print on the same line, but on the line before. Otherwise, it went as expected and printed the extra string before everything else was kept the same.
