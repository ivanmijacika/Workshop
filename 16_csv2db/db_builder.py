#Clyde "Thluffy" Sinclair
#SoftDev  
#skeleton/stub :: SQLITE3 BASICS
#Dec 2020 -- The Time of the Rona

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================

def input_database(table, file):
    with open(file, 'r') as csvfile:
        data = csv.DictReader(csvfile)
        c.execute("CREATE TABLE y6 (code TEXT, mark INTEGER, id INTEGER PRIMARY KEY)")
        c.execute("INSERT INTO y6 ('systems', 75, 1)")
        """for row in data:
            values = ""
            for column in data.fieldnames:
            	print(column)
            	if type(row[column]) == STRING:
            		val = '"'+row[column]+'"'
                values += row[column] + ', '
            values = values[:-2]
            print(values)
            c.execute("INSERT INTO y5 VALUES (" + values + ")")
        """
            
input_database("y6", "courses.csv")
# < < < INSERT YOUR TEAM'S POPULATE-THE-DB CODE HERE > > >


#command = ".open discobandit.db"          # test SQL stmt in sqlite3 shell, save as string
#c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database
