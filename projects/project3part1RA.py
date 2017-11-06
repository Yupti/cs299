import turtle
import csv

def main():
    mags = []
    categories = [0,0,0,0,0,0,0,0,0,0]
    mags = readFile(mags)
    categories = counter(mags, categories)  
    drawing(categories)

def readFile(mags):
    newMags = []
    fileName = "all_month.csv"
    with open(fileName, newline = '') as file:
        reader = csv.reader(file)
        for row in reader:
            mags.append(row[4])
    mags = listCleanse(mags, 'mag')
    mags = listCleanse(mags, '')
    for i in mags:
        val = float(i)
        if val > 0.0:
            newMags.append(val)
    return newMags

def listCleanse(theList, val):
    return [value for value in theList if value != val]

def counter(M, C):
    for i in M:
        if i < 0.7:
            C[0] += 1
        elif i < 1.4:
            C[1] += 1
        elif i < 2.1:
            C[2] += 1
        elif i < 2.8:
            C[3] += 1
        elif i < 3.5:
            C[4] += 1
        elif i < 4.2:
            C[5] += 1
        elif i < 4.9:
            C[6] += 1
        elif i < 5.6:
            C[7] += 1
        elif i < 6.3:
            C[8] += 1
        else:
            C[9] += 1
    return C

def drawing(cats):
    holder = [0.7, 1.4, 2.1, 2.8, 3.5, 4.2, 4.9, 5.6, 6.3, 7.0]
    window = turtle.Screen()
    t = turtle.Turtle()
    t.speed("fastest")
    t.hideturtle()
    t.penup()
    t.goto(-400, -275)
    t.setheading(180)
    t.forward(30)
    t.write(0)
    t.goto(-400, -275)
    t.pendown()
    t.setheading(90)
    
    val2 = 340
    for i in range(10): # vertical draw
        t.forward(60)
        t.setheading(180)
        t.forward(30)
        t.write((val2*(i+1)))
        t.setheading(0)
        t.forward(30)
        t.setheading(90)
        
    t.goto(-400, -275)
    t.setheading(0)
    for i in holder: # horizontal draw
        t.forward(80)
        t.setheading(270)
        t.penup()
        t.forward(30)
        t.write(i)
        t.setheading(90)
        t.forward(30)
        t.setheading(0)
        t.pendown()
    
    t.goto(-400, -275)
    t.setheading(90)
    for i in cats: # for each bar
        val = (i / 3400) * 600
        t.forward(val)
        t.setheading(0)
        t.forward(80)
        t.setheading(270)
        t.forward(val)
        t.setheading(90)

    t.penup()
    t.goto(-400, -275)
    t.forward(300)
    t.setheading(180)
    t.forward(150)
    t.write("# of earthquakes")
    
    t.goto(-400, -275)
    t.setheading(0)
    t.forward(400)
    t.setheading(270)
    t.forward(60)
    t.write("Magnitude of earthquake")

    t.setheading(90)
    t.forward(630)
    t.write("Histogram of Earthquakes (past 30 days)")

    window.exitonclick()
    
if __name__ == "__main__":
    main()
