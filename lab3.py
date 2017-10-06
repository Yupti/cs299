import sys

def main():
   x,y,z = organizedNums()
   print(x,y,z)

   itemList = []
   price = 1.0
   item = input("Enter item name: ")
   tax = float(input("Enter tax rate: "))
   while price > 0:
      price = float(input("Please enter values, and '0' or lower to stop: "))
      if price > 0:
         itemList.append(price)
      else:
         compute(item, tax, itemList)
         
def organizedNums():
   num = 1
   counter = 0
   smallestNum = sys.maxsize
   largestNum = 0
   while num > 0:
      num = int(input("Enter a postive integer, or '0' or lower to exit: "))
      if num <= 0:
         break
      else:
         counter += 1
         if num < smallestNum: # for smallest number
            smallestNum = num
         if largestNum == 0: # for largest number
            largestNum = num
         elif num > largestNum:
            largestNum = num
   if counter == 0:
      return 0,0,0 # case where no numbers were entered
   else:
      return counter, largestNum, smallestNum

def compute(item, tax, *args):
   print("Item:", item, " Tax rate:", tax, "Purchases:", end = ' ')
   total = 0.0
   for arg in args:
      for i in arg:
         print(i, end = '  ')
         total += i
   total = float(total + (total * tax / 100))
   total = round(total, 2)
   print("Total is:", total)
                
                
            
    
