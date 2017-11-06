#import random
#import string
import turtle

def main(): # to call keyGen and substitution encrypt

    barcode("55555-1237")
    #barcode("91768-1234")
    #barcode("20500-0000")

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

    window = turtle.Screen()
    franklin = turtle.Turtle()
    franklin.pensize(2)
    franklin.speed(150)
    
    for i in barCodeList:
        movementVal = 0 
        franklin.setheading(90)
        if i == 1:
            movementVal = 50
            franklin.forward(50) # upwards motion on '1'
        else:
            movementVal = 30
            franklin.forward(30) # upwards motion on '0'
        franklin.penup()
        franklin.setheading(270)
        franklin.forward(movementVal)
        franklin.right(270)
        franklin.forward(4) # rightwards motion
        franklin.pendown()
    window.exitonclick()


if __name__ == "__main__":
    main()
