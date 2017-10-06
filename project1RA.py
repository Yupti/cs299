import random
import time
import math

def main():  
  sentence = input("Enter a sentence to turn into an acronym: ")
  acronymMaker(sentence)
  perfectNumberChecker(6)
  perfectNumberChecker(28)
  perfectNumberChecker(325)
  perfectNumberChecker(496)
  monteCarlo(100)
  monteCarlo(1000)
  monteCarlo(10000)
  
def acronymMaker(sentence):
  acronym = ""
  lists = sentence.split() # splits sentence into parts
  rejected = ["and","by","in","of","on"] # words that are not included in acronym
  for i in lists:
    canPrint = True
    i = i.lower()
    for j in rejected:
      if i == j:
        canPrint = False
    if canPrint == True:
      acronym += i[0].upper() # creates acronym if not a rejected word
  print("Acronym is:", acronym)

def perfectNumberChecker(number):
  numList = [] # for holding the factors
  start = 1
  total = 0
  print("Number for testing is:", number)
  while start != number:
    if number % start == 0: # locates factors of the target number
      numList.append(start)
      total += start
    start += 1
  if total != number: # sum of factors does not equal number
    print("This number is not perfect.")
    return False
  else: # sum of factors equal number
    print(number, "is a perfect number")
    last = numList[-1]
    for i in numList:
      if i == last:
        print(i, "=", number)
      else:
        print(i, "+ ", end = '')
    return True

def monteCarlo(cases):
  count = 0
  caseTemp = cases
  startTime = time.time()
  while caseTemp != 0:
    x = random.uniform(0,1) # picks 2 random points for circle
    y = random.uniform(0,1)
    value = math.sqrt(math.pow(x,2) + math.pow(y,2))
    if value <= 1: # checks if points are within the circle
      count += 1
    caseTemp -= 1
  piValue = 4 * count / cases # calculates pi value
  endTime = time.time() - startTime # calculates elapsed time
  print("Test for", cases, "cases: Count:", count, " Pi Value:", piValue, " Elapsed Time:", endTime)

'''
Enter a sentence to turn into an acronym:  Natural apples by the oranges
Acronym is: NATO

Number for testing is: 6
6 is a perfect number
1 + 2 + 3 = 6
Number for testing is: 28
28 is a perfect number
1 + 2 + 4 + 7 + 14 = 28
Number for testing is: 325
This number is not perfect.
Number for testing is: 496
496 is a perfect number
1 + 2 + 4 + 8 + 16 + 31 + 62 + 124 + 248 = 496

Test for 100 cases: Count: 76  Pi Value: 3.04  Elapsed Time: 0.0001590251922607422
Test for 1000 cases: Count: 755  Pi Value: 3.02  Elapsed Time: 0.0013916492462158203
Test for 10000 cases: Count: 7864  Pi Value: 3.1456  Elapsed Time: 0.01361703872680664
'''
