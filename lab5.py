
def main():
    Names = ['joe','tom','barb','sue','sally']
    Scores = [10,17,20,18,15]
    Ages = [20,17,19,18,22]
    test = makeDict(Names, Scores)
    #print(test)
    for i in test.keys():
        print(i, ":", test.get(i))

def makeDict(list1, list2):
    test = dict(zip(list1,list2))
    return test

if __name__ == "__main__":
    main()
