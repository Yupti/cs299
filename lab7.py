import csv

def main():
    name = "Bob"
    names = ["Joe", "Son","Jack"]
    scores = [87, 79, 100]
    D = dict(zip(names,scores))
    getTotalScore(name, D)
    scoreDictionary()

def getTotalScore(name, D): #D for dictionary
    try:
        found = False
        for i in D.keys():
            if i == name:
                print("Score for", name, "is", D[i])
                return D[i]
        if found == False:
            raise NotFoundError
    except NotFoundError:
        print("ERROR: The name", name, "was not found in the dictionary")

def scoreDictionary():
    nameList = []
    scoreList = []
    book = "grades.csv"
    illegal = 0
    try:
        with open(book, newline = '') as file:
            reader = csv.reader(file)
            next(reader) # testing, hopefully it skips a row
            for row in reader:
                name = ""
                inScoreList = []
                name += row.pop(0) # took out a row.pop(), hopefully is ok
                print("Name:", name)
                nameList.append(name)
                for i in row:
                    inScoreList.append(i)
                scoreList.append(inScoreList) #does what its supposed to
    except InvalidScoreError:
        print("Score is invalid")
        illegal += 1
    print(scoreList)

class Error(Exception):
    pass

class NotFoundError(Error):
    pass

class InvalidScoreError(Error):
    pass

if __name__ == "__main__":
    main()
