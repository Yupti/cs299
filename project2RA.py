import random
import string
import turtle

def main(): # to call keyGen and substitution encrypt


    print("TEST 1")
    substitutionEncrypt("", "face")
    substitutionEncrypt("", "blow")

    print("TEST 2")
    substitutionEncrypt(keyGen(), "face")
    substitutionEncrypt(keyGen(), "blow")

    print("TEST 3")
    substitutionEncrypt("", "wonderful", "python", "java", "doedlugvusu")

    print("TEST 4")
    substitutionEncrypt(keyGen(), "wonderful", "python", "java", "doedlugvusu")


    barcode("91768-1234")

def substitutionEncrypt(key, *args): # for converting word into code word, done
    newWord = ""
    if key == "":
        key = "bpzhgocvjdqswkimlutneryaxf"
    print("Key: ", key)
    for word in args:
        for i in word:
            newWord += key[(ord(i) - 97)]
        print("Word: ", word, " Code Word: ", newWord, "\n")
        newWord = ""

def keyGen(): # for random key generator, done
    defaultKey = "bpzhgocvjdqswkimlutneryaxf"
    randomizedKey = ''.join(random.sample(defaultKey,len(defaultKey)))
    if defaultKey == randomizedKey:
        while defaultKey == randomizedKey:
            randomizedKey = ''.join(random.sample(randomizedKey,len(randomizedKey)))
    return randomizedKey


def barcode(zip): #in progress
    sum = 0
    zipList = []
    barCodeList = [1]
    num = zip.split("-")
    for i in num:
        convertNum = str(i)
        for j in convertNum:
            sum += int(j)
            zipList.append(int(j))
    print(sum)
    sum = sum % 10
    digit = 10 - sum # holds digit to add to end of zip code
    zipList.append(digit)
    for i in zipList:
        if i == 0:
            barCodeList.extend([1, 1, 0, 0, 0])
        elif i == 1:
            barCodeList.extend([0, 0, 0, 1, 1])
        elif i == 2:
            barCodeList.extend([0, 0, 1, 0, 1])
        elif i == 3:
            barCodeList.extend([0, 0, 1, 1, 0])
        elif i == 4:
            barCodeList.extend([0, 1, 0, 0, 1])
        elif i == 5:
            barCodeList.extend([0, 1, 0, 1, 0])
        elif i == 6:
            barCodeList.extend([0, 1, 1, 0, 0])
        elif i == 7:
            barCodeList.extend([1, 0, 0, 0, 1])
        elif i == 8:
            barCodeList.extend([1, 0, 0, 1, 0])
        elif i == 9:
            barCodeList.extend([1, 0, 1, 0, 0])
    barCodeList.append(1)

    print(barCodeList)
    franklin = turtle.Turtle()
    franklin.pensize(2)
    list1 = [30, 30, 20, 50, 20]
    x = 4
    for i in barCodeList:
        franklin.setheading(90)
        if i == 1:
            franklin.forward(50) # upwards
        else:
            franklin.forward(30)
        franklin.penup()
        franklin.home()
        franklin.right(0)
        franklin.forward(x) # rightwards
        franklin.pendown()
        x += 4
    franklin.done()


if __name__ == "__main__":
    main()
