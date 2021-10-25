"""
Waahoos: Alejandro Alonso, Ivan Mijacika, William Chen
SoftDev
K16 -- All About Database -- Sqlite3
2021-10-25
"""

import csv, sqlite3

con = sqlite3.connect("discobandit.db") # change to 'sqlite:///your_filename.db'
cur = con.cursor()

def crt_table(file, t):
    """
    creates a sql table named t given a csv file with 3 columns in discobandit.dbg
    """
    with open(file,'r') as fin:
        data = csv.DictReader(fin)
        #print("***DIAG: dictreader obj***")
        headers = data.fieldnames
        headers_str = "(" + ", ".join(data.fieldnames) + ")"
        vals = [(row[headers[0]], row[headers[1]], row[headers[2]]) for row in data] #transferring dictreader values to a 2d array
        #print("***DIAG: vals***")

    cur.execute(f"CREATE TABLE {t} {headers_str};") # creates table
    cur.executemany(f"INSERT INTO {t} {headers_str} VALUES (?, ?, ?);", vals) #for row of values in list object vals, inserts the values into the table

crt_table("students.csv", "students")
crt_table("courses.csv", "courses")

con.commit()
con.close()