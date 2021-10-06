"""
Ishraq Mahid, Gavin McGinley, Ivan Mijacika - Cool Dogs
Softdev
k06 -- Weighted Probability
2021-9-28
#SUMMARY OF DISCUSSION:
We mainly worked together figuring out how to read in CSVs, and conceptualizing how to best do weighted randomness.
#QUESTIONS 
What is the better way to do weighted averages? Our group felt that utilizing a list or dictionaries 
this manner had to be vastly inferior and ineffecient compared to the best solution,
despite not knowing what the best solution is.
#Discoveries:
We mainly just figured out how reading in CSV files works.
#Comments:
This method also limits scalability. If sig figs increase, some code has to be created
in response.
"""


def csvReader():
    import csv

    #Reads CSV into program as "reader"
    csv_file = open("occupations.csv")
    reader = csv.reader(csv_file)
    return reader

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

def generateListStr(highlight):
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
                

    return returnString


if __name__ == "__main__":
    print(weighted())
