# Team Toast
# Ivan Mijacika, Rayat Roy, Haotian Gan (Duckies: Cinnamon, Bob, Zippy Frog)
# SoftDev
# K13
# 10-08-2021

import csv, random


def readfile(filename):
    """Function to read csv file and transfer it to an approriate dictionary"""
    file = open(filename)
    csvreader = csv.reader(file)
    next(csvreader) #Skip first line
    occupations = {}
    for row in csvreader:
        if row[0] != "Total": #Don't include line with the total
            occupations[row[0]] = row[1], row[2]
    file.close()
    return occupations


def generateRandom(occupations):
    """Using the weights provided in percentages, generate a randomly selected occupation"""
    ran = random.random() * 100
    for row in occupations:
        holder = occupations.get(row)[0]
        ran -= float(holder)
        if ran <= 0:
            return row
    return "Unemployed" #if user never reaches 0, they are unemployed   


from flask import Flask, render_template
app = Flask(__name__) #create instance of class Flask

@app.route("/occupyflaskst")       #assign fxn to route
def hello_world():
    file = readfile("data/occupations.csv")
    choice = generateRandom(file)
    return render_template('tablified.html', choice=choice, occupations=file)

app.run(debug=True)