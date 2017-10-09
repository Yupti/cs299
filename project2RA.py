import random
import string
import turtle

def main():
    print("test")
    for i in range(26):
        print(i)
    barcode("Test")

def keyGen():
    key = ""
    found = False
    totalLetters = 0
    for i in range(26):
        letter = random.choice(string.ascii_letters)
        #for i in key:
            #if i == letter:


def barcode(zip): #in progress
    '''
    sum = 0
    num = zip.split("-")
    zipLine = ""
    for i in num:
        zipLine += i
        sum += int(i)
    sum = sum % 10
    digit = 10 - sum # holds digit to add to end of zip code

    # area for deciding digits to pass to be drawn
    '''
    franklin = turtle.Turtle()
    franklin.pensize(5)
    list1 = [30, 30, 20, 50, 20]
    x = 10
    for i in list1:
        franklin.setheading(90)
        franklin.forward(i) # upwards
        franklin.penup()
        franklin.home()
        franklin.right(0)
        franklin.forward(x) # rightwards
        franklin.pendown()
        x += 10


    franklin.done()

if __name__ == "__main__":
    main()
