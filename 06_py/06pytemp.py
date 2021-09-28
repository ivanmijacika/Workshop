import random
import csv

def readMethod():
    with open('FILENAME', newline='') as csvfile:
        jobReader = csv.reader(csvfile, delimeter='', quotechar='|') # <== what is quotechar, delimeter
        for row in jobReader:
            print(', '.join(row))  # <== return formatting

#use read, realine, or readlines
#text reader vs csv
#.append if adding to a list
