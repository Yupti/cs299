def main():  
  sentence = input("Enter a sentence to turn into an acronym")
  acronymMaker(sentence)

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
