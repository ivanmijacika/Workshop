## Ivan Mijacika
## SoftDev
## K05 -- Trio Amalgamate Code
## 2021-09-28

# SUMMARY OF TRIO DISCUSSION
# We all already had our own code from our previous groups,
# so we compared to see what similarities we had.
# We exchanged emails
# We discussed how to convert our lists into dictionaries
# We concluded that after following the template we could use .get
# We helped a memebr set up their sobmodule

# DISCOVERIES
# Making a small guess change and then running isn't efficient
# .get() returns the desired value from your dictionary
# Dictionaries are useful for storing and accesing related data

# QUESTIONS
# What advantages do dictionaries have over lists?
#

# COMMENTS
#

Names = {
    'pd1': ['Emma', 'Shriya', 'William', 'Aaron', 'Shyne'],
    'pd2': ['studentA', 'studentB', 'studentC', 'studentD']
}

import random

def printName():
    # input variable is used so that user can choose which class to pick a name from
    period = input('Pick a period (Input 1 or 2) Or select 3 for a name from either: ')
    if period == '1':
        print(Names.get('pd1')[random.randint(0,len(Names.get('pd1')) - 1)])
    elif period == '2':
        print(Names.get('pd2')[random.randint(0,len(Names.get('pd2')) - 1)])
    # if the period is 3 print names from both period 1 and 2
    elif period == '3':
        total = Names.get('pd1') + Names.get('pd2')
        print(total[random.randint(0, len(total) - 1)])
    # the 'else' below forces the user to pick an option if they didn't follow the rules
    else:
        print('NOT AN OPTION')
        printName()
