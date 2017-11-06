import csv
import urllib.request

def main():
    Q1()
    Q2()
    Q3()

def Q1():
    print("Q1")
    book = open('book.txt','r', newline = '')
    myBook = open('myBook.txt','w', newline = '')
    for line in book:
        myBook.write(line)
    book.close()
    myBook.close()

def Q2():
    print("Q2")
    pList = []
    fileName = "planets.csv"
    newFileName = "myPlanets.csv"
    with open(fileName,newline = '') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[10] != '\tMoon':
                moons = int(row[10])
                moons += 2
                row[10] = str(moons)
            pList.append(row)

    with open(newFileName,'w',newline = '') as file:
        writer = csv.writer(file)
        writer.writerows(pList)

def Q3():
    print("Q3")
    page = urllib.request.urlopen('https://www.nytimes.com/')
    data = page.readlines()
    print(data[0:10])
    
if __name__ == "__main__":
    main()
