def main():  
  #sentence = input("Enter a sentence to turn into an acronym: ")
  #acronymMaker(sentence)
  #perfectNumberChecker(28)

def acronymMaker(sentence):
  acronym = ""
  lists = sentence.split()
  rejected = ["and","by","in","of","on"]
  for i in lists:
    canPrint = True
    for j in rejected:
      if i == j:
        canPrint = False
    if canPrint == True:
      acronym += i[0].upper()
  print(acronym)

def perfectNumberChecker(number):
  numList = [] # for holding the factors
  start = 1
  total = 0
  print("Number for testing is:", number)
  while start != number:
    if number % start == 0:
      numList.append(start)
      total += start
    start += 1
  if total != number:
    print("This number is not perfect.")
  else:
    print(number, "is a perfect number")
    last = numList[-1]
    for i in numList:
      if i == last:
        print(i, "=", number)
      else:
        print(i, "+ ", end = '')
