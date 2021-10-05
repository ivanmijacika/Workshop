# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2021

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()

#Has a string before returning __name__, but this time it says something different (same idea though)
#The rest of hello_world() is the same
#Has an if statement now that check whether the __name__ is __main__, which should be true
#The if statement now determines whether the last to lines are called, meaning that if it is true the debuger is turned on and app.py is ran, otherwise not

#RESULTS

#The stuff printed in the terminal is slight5ly different, and it turns on the debugger and runs (because __name__ is __main__)
