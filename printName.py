import random
pd1 = ["Ivan", "Gavin", "Ishraq", "Michael", "William", "David", "Richard", "Joseph", "Thomas", "Charles", "Christopher", "Daniel", "Matthew", "Anthony", "Mark", "Mary", "Patricia", "Jennifer", "Linda", "Elizabeth"]
pd2 = ["James", "Robert", "John", "Donald", "Steven", "Paul", "Andrew",  "Joshua", "Maria", "Nushi", "Mohammed", "Jose", "Muhammad", "Mohamed", "Wei", "Mohammad", "Ahmed", "Yan", "Ali", "Li", "Abdul", "Ana"]
#We didn't have a class list and not everyone had a useful display name on Github so we just used common names^

def printName():
    if random.getrandbits(1):
        print(randomStudent(pd1))
    else:
        print(randomStudent(pd2))
    
            
def randomStudent(periodList):
    return periodList[random.randint(0,len(periodList)-1)]

printName()
