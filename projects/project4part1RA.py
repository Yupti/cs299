import random

class ComboLock:

	# initializes the variables to 0 or empty
	def __init__(self, newCombo):
		self.combo = newCombo
		self.userComboTurn = []
		self.user = []
		self.position = 0
		print("You are at the starting position, 0")

	def checkCombo(self):
		print("Combination is:", self.combo)

	def reset(self):
		self.userComboTurn = [] 
		self.user = []
		self.position = 0 		
		print("You have reset the entire lock, now at 0")

	def turnLeft(self, num):
		print("Turning", num, "ticks left")
		self.userComboTurn.append("left")
		self.position -= num
		if self.position < 0:
			self.position += 10
		print("You are at position:", self.position)
		self.user.append(self.position)

	def turnRight(self, num):
		print("Turning", num, "ticks right")
		self.userComboTurn.append("right")
		self.position += num
		if self.position > 9:
			self.position -= 10
		print("You are at position:", self.position)
		self.user.append(self.position)

	def open(self):
		print("Attempting to open lock...")
		print("User:", self.user)
		print("Combo:", self.combo)

		if len(self.userComboTurn) == 3:
			if (self.userComboTurn[0] == self.userComboTurn[2] == "right") and (self.userComboTurn[1] == "left"):
				if self.user == self.combo:
					print("Opened lock successfully!")
				else:
					print("Failed to open lock, please reset.")
			else:
				print("You have turned the lock in the wrong order, please reset.")
		else:
			print("You have turned the lock too many or too few times, please reset.")

def main():

	print("Test #1")
	test = ComboLock([2,9,1])
	test.checkCombo()
	test.turnRight(2)
	test.turnLeft(3)
	test.turnRight(1)
	test.open()
	test.reset()
	test.checkCombo()
	test.turnRight(2)
	test.turnLeft(3)
	test.turnRight(2)
	test.open()

	print("\nTest #2")
	test2 = ComboLock([2,9,1])
	test2.checkCombo()
	test2.turnRight(2)
	test2.turnLeft(3)
	test2.open()
	test.reset()
	test.checkCombo()
	test.turnRight(2)
	test.turnLeft(3)
	test.turnLeft(2)
	test.open()

	print("\nTest #3")
	test3 = ComboLock([6, 3, 4])
	test3.checkCombo()
	test3.turnRight(6)
	test3.turnLeft(3)
	test3.turnRight(1)
	test3.open()

if __name__ == '__main__':
	main()

'''
OUTPUT
Test #1
You are at the starting position, 0
Combination is: [2, 9, 1]
Turning 2 ticks right
You are at position: 2
Turning 3 ticks left
You are at position: 9
Turning 1 ticks right
You are at position: 0
Attempting to open lock...
User: [2, 9, 0]
Combo: [2, 9, 1]
Failed to open lock, please reset.
You have reset the entire lock, now at 0
Combination is: [2, 9, 1]
Turning 2 ticks right
You are at position: 2
Turning 3 ticks left
You are at position: 9
Turning 2 ticks right
You are at position: 1
Attempting to open lock...
User: [2, 9, 1]
Combo: [2, 9, 1]
Opened lock successfully!

Test #2
You are at the starting position, 0
Combination is: [2, 9, 1]
Turning 2 ticks right
You are at position: 2
Turning 3 ticks left
You are at position: 9
Attempting to open lock...
User: [2, 9]
Combo: [2, 9, 1]
You have turned the lock too many or too few times, please reset.
You have reset the entire lock, now at 0
Combination is: [2, 9, 1]
Turning 2 ticks right
You are at position: 2
Turning 3 ticks left
You are at position: 9
Turning 2 ticks left
You are at position: 7
Attempting to open lock...
User: [2, 9, 7]
Combo: [2, 9, 1]
You have turned the lock in the wrong order, please reset.

Test #3
You are at the starting position, 0
Combination is: [6, 3, 4]
Turning 6 ticks right
You are at position: 6
Turning 3 ticks left
You are at position: 3
Turning 1 ticks right
You are at position: 4
Attempting to open lock...
User: [6, 3, 4]
Combo: [6, 3, 4]
Opened lock successfully!

'''