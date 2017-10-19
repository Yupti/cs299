def main():
    Names = ['joe','tom','barb','sue','sally']
    Scores = [10,17,20,18,15]
    Ages = [20,17,19,18,22]
    scoreDict = makeDict(Names, Scores)
    print("Results of the dictionary")
    for i in scoreDict.keys():
        print(i, ":", scoreDict.get(i))
    q3(Names, Scores, Ages)
    q4(scoreDict)
    getMedianScore(scoreDict)
    getScore('john', scoreDict)
    getScore('ana', scoreDict)

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
    print(firstSet & frozenSet)

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

def getMedianScore(tDict):
    print("Q5")
    counter = 0
    median = 0.0
    print("Adding scores of students in dictionary to calculate median...")
    for i in tDict.keys():
        counter += 1
        median += tDict.get(i)
    median /= counter
    print("Median of scores is:", median)

def getScore(name, tDict):
    print("Q6")
    print("Locating score for student", name)
    if name in tDict:
        print("Score of student", name, "is", tDict.get(name))
        return tDict.get(name)
    else:
        print("The student", name, "was not found")
        return -1

if __name__ == "__main__":
    main()
