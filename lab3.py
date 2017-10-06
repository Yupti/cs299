import sys

def main():
   x,y,z = organizedNums(0)
   print(x,y,z)
   x,y,z = organizedNums(5, -1)
   print(x,y,z)
   x,y,z = organizedNums(5, 6, 12, 8, 2, 18, 21, 3, -5)
   print(x,y,z)

   shopList("Fruits", 8, 80, 125, 45.5)
   shopList("Furniture", 10.5, 950)
   shopList("Toys", 7.5, 12, 5.5, 6.5, 7.5, 9.0)
         
def organizedNums(*args):
   counter = 0
   smallestNum = sys.maxsize
   largestNum = 0
   for arg in args:
      if arg <= 0:
         break
      else:
         counter += 1
         if arg < smallestNum: # for smallest number
            smallestNum = arg
         if largestNum == 0: # for largest number
            largestNum = arg
         elif arg > largestNum:
            largestNum = arg
   if counter == 0:
      return 0,0,0 # case where no numbers were entered
   else:
      return counter, largestNum, smallestNum

def shopList(item, tax, *args):
   print("Item:", item, " Tax rate:", tax, "Purchases:", end = ' ')
   total = 0.0
   for arg in args:
      print(arg, end = '  ')
      total += arg
   total = float(total + (total * tax / 100))
   total = round(total, 2)
   print("Total is:", total)
                
if __name__ == "__main__":
   main()

'''
0 0 0
1 5 5
8 21 2
Item: Fruits  Tax rate: 8 Purchases: 80  125  45.5  Total is: 270.54
Item: Furniture  Tax rate: 10.5 Purchases: 950  Total is: 1049.75
Item: Toys  Tax rate: 7.5 Purchases: 12  5.5  6.5  7.5  9.0  Total is: 43.54
'''
    
