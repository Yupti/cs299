class Animal:
	def __init__(self):
		print("A new animal has been created.")
	def sleep(self):
		print("An animal sleeps.")
	def eat(self):
		print("An animal eats.")

class Bird(Animal):
	def __init__(self):
		Animal.__init__(self)
		print("A new bird has been created.")
	def sleep(self):
		print("A bird sleeps.")
	def eat(self):
		print("A bird eats.")

def main():
	a = Animal()
	b = Bird()
	print("")
	a.sleep()
	a.eat()
	b.sleep()
	b.eat()

if __name__ == '__main__':
	main()