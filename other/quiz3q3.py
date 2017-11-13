class Point:
	def __init__(self, xc = 0, yc = 0):
		self.x = xc
		self.y =yc
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

def main():
	p1 = Point(3,5)
	p2 = Point(2,0)
	if (p2 == p1):
		print('two points together')
	else:
		print('two points apart')
	p1 = p1 + p2
	print('new p1 is: ', p1.get())

if __name__ == '__main__':
	main()