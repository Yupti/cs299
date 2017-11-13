class Point:
	def __init__(self, xc = 0, yc = 0):
		self.x = xc
		self.y = yc
	def setx(self, xc):
		self.x = xc
	def sety(self, yc):
		self.y = yc
	def get(self):
		return Point(self.x, self.y)
	def move(self, dx, dy):
		self.x = self.x + dx
		self.y = self.y + dy
	def __eq__(self, other):
		return self.x == other.x and self.y == other.y
	def __add__(self, other):
		self.x += other.x
		self.y += other.y
		return Point(self.x, self.y)
	def __str__(self):
		return "(" + str(self.x) + "," + str(self.y) + ")"

class Point3D(Point):
	thisSet = ()
	def __init__(self, newSet):
		self.thisSet = newSet
	def getZ(self):
		print(self.thisSet[2])
	def get(self):
		print(self.thisSet)
	def __eq__(self, points):
		return self.thisSet == points
	def __str__(self, thing):
		return str(thing)


def main():
	# Question 3
	p1 = Point(3,5)
	p2 = Point(2,0)
	if (p2 == p1):
		print('two points together')
	else:
		print('two points apart')
	p1 = p1 + p2
	print('new p1 is: ', p1.get())
	
	# Question 5
	a = Point3D((12,7,11))
	b = Point3D((12,11,7))
	if (a == b):
		print("They are equal.")
	else:
		print("The are not equal.")
	a.getZ()
if __name__ == '__main__':
	main()