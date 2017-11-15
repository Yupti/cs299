def main():
	print("Q1")
	print("Reversed string for 'abc'")
	print(reverse("abc"))
	print("")

	print("Q2")
	print("Recursive for pattern(0)")
	pattern(0)
	print("")
	print("Recursive for pattern(1)")
	pattern(1)
	print("")
	print("Recursive for pattern(2)")
	pattern(2)
	print("")
	print("Recursive for pattern(3)")
	pattern(3)
	print("\n")

	print("Q3")
	print("Generic Sort")
	print("Integer list in descending order:")
	aList = [3,1,8,0,23,11,9,78]
	generic_sort(descend, aList)
	print("")
	print("String list in ascending order:")
	aList = ["Kate", "Aaron", "Zack", "Joe", "Joey", "Brandon"]
	generic_sort(ascend, aList)
	print("")
	print("Tuple list in ascending order, duplicates based on second value:")
	aList = [("Kate", 2), ("Aaron", 7), ("Kate", 3), ("Zack", 9), ("Brandon", 3), ("Aaron", 2)]
	generic_sort(ascend, aList)
	print("")

	print("Q4")
	print("Mapping/Filtering Lists")
	bList = [x for x in range(1, 101)]
	print("Base list:")
	print(bList)
	print("Doubled:")
	print(list(map(double, bList)))
	print("")

	print("Base list:")
	print(bList)
	cList = [x for x in bList[0:101:2]]
	print("Odd Elements Squared:")
	print(list(map(squared, cList)))
	print("")

	print("Base list:")
	print(bList)
	print("Prime List:")
	print(list(filter(isPrime, bList)))


def reverse(word):
	if word == "":
		return word
	else:
		return reverse(word[1:]) + word[0]

def pattern(num):
	if num == 0:
		print(num, end = ' ')
		return
	else:
		pattern(num - 1)
		print(num, end = ' ')
		pattern(num - 1) 

def ascend(aList):
	newList = []
	while aList:
		smallest = min(aList)
		index = aList.index(smallest)
		newList.append(aList.pop(index))
	print(newList)

def descend(aList):
	newList = []
	while aList:
		smallest = max(aList)
		index = aList.index(smallest)
		newList.append(aList.pop(index))
	print(newList)

def generic_sort(gFunction, aList):
	return gFunction(aList)

def double(x):
	return x*2

def squared(x):
	return x**2

def isPrime(n):
	for i in range(2,int(n**0.5)+1):
		if n%i==0:
			return False
	return True

if __name__ == '__main__':
	main()

'''
Q1
Reversed string for 'abc'
cba

Q2
Recursive for pattern(0)
0 
Recursive for pattern(1)
0 1 0 
Recursive for pattern(2)
0 1 0 2 0 1 0 
Recursive for pattern(3)
0 1 0 2 0 1 0 3 0 1 0 2 0 1 0 

Q3
Generic Sort
Integer list in descending order:
[78, 23, 11, 9, 8, 3, 1, 0]

String list in ascending order:
['Aaron', 'Brandon', 'Joe', 'Joey', 'Kate', 'Zack']

Tuple list in ascending order, duplicates based on second value:
[('Aaron', 2), ('Aaron', 7), ('Brandon', 3), ('Kate', 2), ('Kate', 3), ('Zack', 9)]

Q4
Mapping/Filtering Lists
Base list:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
Doubled:
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192, 194, 196, 198, 200]

Base list:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
Odd Elements Squared:
[1, 9, 25, 49, 81, 121, 169, 225, 289, 361, 441, 529, 625, 729, 841, 961, 1089, 1225, 1369, 1521, 1681, 1849, 2025, 2209, 2401, 2601, 2809, 3025, 3249, 3481, 3721, 3969, 4225, 4489, 4761, 5041, 5329, 5625, 5929, 6241, 6561, 6889, 7225, 7569, 7921, 8281, 8649, 9025, 9409, 9801]

Base list:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
Prime List:
[1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
'''