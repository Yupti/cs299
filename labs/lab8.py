def main():
	print(reverse("abc"))
	pattern(3)
	aList = ["Kate", "Aaron", "Zack", "Joe", "Joey", "Brandon"]
	generic_sort(ascend, aList)
	aList = [3,1,8,0,23,11,9,78]
	generic_sort(descend, aList)

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

if __name__ == '__main__':
	main()