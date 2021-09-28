import random
pd1 = ["Ivan", "Gavin", "Ishraq", "Michael", "William", "David", "Richard", "Jo>
pd2 = ["James", "Robert", "John", "Donald", "Steven", "Paul", "Andrew",  "Joshu>
#We didn't have a class list and not everyone had a useful display name on Gith>

def printName():
    if random.getrandbits(1):
        print(randomStudent(pd1))
    else:
        print(randomStudent(pd2))


def randomStudent(periodList):
    return periodList[random.randint(0,len(periodList)-1)]

printName()
