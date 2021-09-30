"""
Ivan Mijacika, Gavin McGinley, Ishraq Mahid - "Cool Dogs"
Softdev
k06 -- File Reading + Weighted Probability
2021-9-28
"""

"""
#SUMMARY OF TRIO DISCUSSION
We initially had to review how to read a csv file in order to make use of the
data, and then we discussed some methods for solving the problem. One of our
alternate ideas was to have a list with job categories as objects of the list,
with the number of repetitions being related to the percent. We finally settled
on changing the percents to integers and working with that.

#DISCOVERIES
We looked at the csv module documentation and figured out how to use it.
Learned a method of doing a weighted average

#QUESTIONS
Although we were able to come up with a solution, it felt a little tedious/inneficient.
Is there a better way to do this?

#COMMENTS
Created to work with decimals up to the tenths place
"""

def weighted():
    import csv
    import random

    #Reads CSV into program as "reader"
    csv_file=open("occupations.csv")
    reader=csv.reader(csv_file)
    next(reader) #skip 1st

    wdict={}
    for row in reader:
        wdict[row[0]]=float(row[1]) #copies over the data from the csv into a dictionary
   
    #percentages represented out of 1000 to stay within integers
    num=random.randint(1,998)
    total=0;

    #Likeliness of passing total is proportional to its percentage
    for x in wdict.keys():
        total=total+(wdict[x]*10)
        if total>=num:
            print(x)
            break
weighted()
