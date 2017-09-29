string = "This feels of food"
acronym = ""
lists = string.split()
rejected = ["and","by","in","of","on"]
for i in lists:
  canPrint = True
  for j in rejected:
    if i == j:
      canPrint = False
  if canPrint == True:
    acronym += i[0].upper()
print(acronym)