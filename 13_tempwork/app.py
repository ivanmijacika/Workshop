def csvReader():
    import csv

    csv_file = open("occupations.csv")
    reader = csv.reader(csv_file)
    return reader

#####
def weighted():
    import random

    reader = csvReader()
    #skips first line
    next(reader)

    #Adds CSV info to dictionary
    wdict={}
    for row in reader:
        wdict[row[0]]=float(row[1])

    #Randomly generates number    
    num=random.randint(1,998) #instead of putting 998, we can also input total to possibly improve scalabiliyt?
    total=0

    #Likeliness of passing total is proportional to its percentage
    for x in wdict.keys():
        total=total+(wdict[x]*10)
        if total>=num:
            return(x)

def generateTableStr(highlight):
    reader = csvReader()

    #skips first line
    next(reader)

    #Adds CSV info to dictionary
    returnString = ""
    for row in reader:
        
        if row[0] != "Total":
            if(highlight and row[0] == highlight):
                    returnString+="<mark>"
                    returnString += row[0] + "</mark>" + "<br>"
            else:
                returnString += row[0] + "<br>"

