import math

def main():
    q1()
    #q2()
    q3()
    q4()
    q5()

    
def q1():
    num = 35.6
    print(math.sqrt(num))

def q2(): #idk
    primeList = [i for i in range(2,20,isPrime(i))]

def isPrime(num): #idk
    for i in range(2,num):
        if (num % i) == 0:
            return False
    else:
        return True

def q3():
    L = [("Ted",9),("Alice",10),("Aaron", 11)] #list of tuple
    L.append(("Brandon", 12))
    print(L)
    L.remove(("Alice", 10))
    print(L)
    ave = 0.0
    counter = 0
    for i in L:
        ave += i[1]
        counter += 1
    print(ave / counter)
    tup = L.pop(0)
    L.append(tup)
    print(L)

def q4():
    aList = ["Ted","Alice","Mi"]
    aList.sort()
    print(aList)
    aList.insert(2,"David")
    sorted(aList)
    print(aList)

    names = ["Ted","Alice","David","Mi"]
    bonus = [4,5,1]
    print(list(zip(names,bonus)))

def q5():
    names = ["Ted","Emily","Brad","Sue"]
    grades = [10,9,9,11]
    email = ["ted@cpp.edu","emily@cpp.edu","brad@cpp.edu","sue@cpp.edu"]
    book = dict(zip(names,grades))
    test = zip(names,grades)
    book2 = dict(zip(test,email))
    print(book)
    print(book2)
    for i in book.keys():
        book[i] += 1
    print(book)
        
    
if __name__ == '__main__':
    main()
    
