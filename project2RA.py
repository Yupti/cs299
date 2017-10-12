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
        key = "bpzhgocvjdqswkimlutneryaxf" # default key
    print("Key: ", key + "\n")
    for word in args:
        for i in word:
            newWord += key[(ord(i) - 97)] # converts letter in word with a letter in key
        print("Word: ", word, " Code Word: ", newWord, "\n")
        newWord = ""

def keyGen(): # for random key generator
    defaultKey = "bpzhgocvjdqswkimlutneryaxf"
    randomizedKey = ''.join(random.sample(defaultKey,len(defaultKey))) # randomizes the default key
    if defaultKey == randomizedKey:
        while defaultKey == randomizedKey: # case where default and randomkey happen to be the same
            randomizedKey = ''.join(random.sample(randomizedKey,len(randomizedKey)))
    return randomizedKey


def barcode(zip): 
    sum = 0
    zipList = []
    barCodeList = [1]
    num = zip.split("-") # splits zip code
    for i in num: # uses all integers that are separated
        convertNum = str(i)
        for j in convertNum:
            sum += int(j) # holds sum for check sum value
            zipList.append(int(j)) # adds integer to convert to barcode
    sum = sum % 10
    digit = 10 - sum # holds digit to add to end of zip code
    zipList.append(digit)
    for i in zipList: # for appending integer barcodes
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

    franklin = turtle.Turtle()
    franklin.pensize(2)
    x = 4
    for i in barCodeList:
        franklin.setheading(90)
        if i == 1:
            franklin.forward(50) # upwards motion on '1'
        else:
            franklin.forward(30) # upwards motion on '0'
        franklin.penup()
        franklin.home()
        franklin.right(0)
        franklin.forward(x) # rightwards motion
        franklin.pendown()
        x += 4
    franklin.done()


if __name__ == "__main__":
    main()
