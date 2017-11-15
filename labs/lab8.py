def main():
	print(reverse("abc"))
	pattern(3)

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

if __name__ == '__main__':
	main()