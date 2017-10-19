def main():
    q1()
    Names = ['joe','tom','barb','sue','sally']
    Scores = [10,17,20,18,15]
    Ages = [20,17,19,18,22]
    scoreDict = makeDict(Names, Scores)
    print("Results of the dictionary")
    for i in scoreDict.keys():
        print(i, ":", scoreDict.get(i))
    print("\n")
    q3(Names, Scores, Ages)
    q4(scoreDict)
    getMedianScore(scoreDict)
    getScore('john', scoreDict)
    getScore('ana', scoreDict)

def q1():
    print("Q1")
    L1 = [1,2,3,4,5]
    L2 = [2,3,4,5,1,0]
    L3 = ["1","2","3","4","5"]
    print("L1 contains:", L1, "\nL2 contains:", L2, "\nL3 contains:", L3)
    print("L1 < L2:", L1 < L2)
    print("L1 != L2:", L1 != L2)
    print("L1 > L3: unable to compare, one has str, one has int")
    print("L1 and L2:", L1 and L2)
    print("not L3:", not L3)
    print("not []:", not [])
    L1 = [1,2]
    L2 = [1,2]
    L3 = L1
    print("L1 = [1,2], L2 = [1,2], L3 = L1")
    print("L1 is L2:", L1 is L2)
    print("L1 is L3:", L1 is L3)
    sentence = "Hello, Welcome to Python"
    print("sentence set to:", sentence)
    print("Python in sentence:", "Python" in sentence)
    print("min('Python'):", min("Python"))
    seasons = ['Spring','Summer','Fall','Winter']
    print("seasons contains:", seasons)
    print("list(enumerate(seasons, start = 1)):", list(enumerate(seasons, start = 1)), "\n")
    
def makeDict(list1, list2):
    print("Q2")
    test = dict(zip(list1,list2))
    return test

def q3(list1, list2, list3):
    print("Q3")
    firstSet = set()
    aList = []
    for (a,b) in zip(list1,list2):
        tup = (a, b)
        firstSet.add(tup)
    for (a,b) in zip(list1,list3):
        tup = (a, b)
        aList.append(tup)
    frozenSet = frozenset(aList)
    print("Intersection of the set and frozenset")
    print(firstSet & frozenSet, "\n")

def q4(tDict):
    print("Q4")
    print("Adding entry 'john' with a score of 19...")
    tDict['john'] = 19
    print("Adding existing entry 'sue' with a score of 20...")
    tDict['sue'] = 20
    print("Updating entry 'sally' with a score of 19...")
    tDict['sally'] = 19
    print("Removing entry 'tom' and his score from the dictionary...")
    tDict.pop('tom')
    print("Printing current students and scores in alphabetical order.")
    for i in sorted(tDict.items()):
        print(i)
    print("\n")

def getMedianScore(tDict):
    print("Q5")
    counter = 0
    median = 0.0
    print("Adding scores of students in dictionary to calculate median...")
    for i in tDict.keys():
        counter += 1
        median += tDict.get(i)
    median /= counter
    print("Median of scores is:", median, "\n")

def getScore(name, tDict):
    print("Q6")
    print("Locating score for student", name)
    if name in tDict:
        print("Score of student", name, "is", tDict.get(name), "\n")
        return tDict.get(name)
    else:
        print("The student", name, "was not found\n")
        return -1

if __name__ == "__main__":
    main()

'''
Q1
L1 contains: [1, 2, 3, 4, 5] 
L2 contains: [2, 3, 4, 5, 1, 0] 
L3 contains: ['1', '2', '3', '4', '5']
L1 < L2: True
L1 != L2: True
L1 > L3: unable to compare, one has str, one has int
L1 and L2: [2, 3, 4, 5, 1, 0]
not L3: False
not []: True
L1 = [1,2], L2 = [1,2], L3 = L1
L1 is L2: False
L1 is L3: True
sentence set to: Hello, Welcome to Python
Python in sentence: True
min('Python'): P
seasons contains: ['Spring', 'Summer', 'Fall', 'Winter']
list(enumerate(seasons, start = 1)): [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')] 

Q2
Results of the dictionary
joe : 10
tom : 17
barb : 20
sue : 18
sally : 15


Q3
Intersection of the set and frozenset
{('tom', 17), ('sue', 18)} 

Q4
Adding entry 'john' with a score of 19...
Adding existing entry 'sue' with a score of 20...
Updating entry 'sally' with a score of 19...
Removing entry 'tom' and his score from the dictionary...
Printing current students and scores in alphabetical order.
('barb', 20)
('joe', 10)
('john', 19)
('sally', 19)
('sue', 20)


Q5
Adding scores of students in dictionary to calculate median...
Median of scores is: 17.6 

Q6
Locating score for student john
Score of student john is 19 

Q6
Locating score for student ana
The student ana was not found
'''
