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
import csv, random

csv_file = open("occupations.csv")

reader = csv.DictReader(csv_file)

#Taking data from csv and placing into db
workforce_dict = {}
tickets = []

for row in reader:
    workforce_dict[row['Job Class']] = float(row['Percentage'])
    #changes the percentage into an integer out of 1000 so that it's easier to use
    percentage = int(float(row['Percentage'])*10)
    for i in range(percentage):
        if(row['Job Class'] != 'Total'):
            tickets.append(row['Job Class'])

###Gets randomJob, weighted
def randomJob(list):
    return random.choice(list)

print(randomJob(tickets))
