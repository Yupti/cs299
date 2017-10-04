import sys

def main():
   x,y,z = organizedNums()
   print(x,y,z)

def organizedNums():
    num = 1
    counter = 0
    smallestNum = sys.maxsize
    largestNum = 0
    while num != 0:
        num = int(input("Enter a postive integer, or '0' to exit: "))
        if num < 0:
            print("Cannot add, number is not positive")
        elif num == 0:
            break
        else:
            counter += 1
            if num < smallestNum: # for smallest number
                smallestNum = num
            if largestNum == 0: # for largest number
                largestNum = num
            elif num < smallestNum:
                largestNum = num
    if counter == 0:
        return 0,0,0 # case where no numbers were entered
    else:
        return counter, largestNum, smallestNum
                
                
                
            
    
