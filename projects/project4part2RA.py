class Question:

	def __init__(self):
		self.question = ""
		self.answer = ""

	def setText(self, questionText):
		self.question = questionText

	def setAnswer(self, correctResponse):
		self.answer = correctResponse

	def getAnswer(self):
		return self.answer

	def checkAnswer(self, response):
		if self.answer == response:
			print("Correct!")
		else:
			print("Sorry, the answer is: ", self.getAnswer())
		print("")
		

	def display(self):
		print(self.question)

class ChoiceQuestion(Question):

	def __init__(self, question):
		self.choiceNum = 0
		self._choice = [] # to show choices for user to see
		Question.setText(self, question)

	# for multiple choice questions
	def addChoice(self, choice, correct):
		self.choiceNum += 1
		self._choice.append(str(self.choiceNum) + ". " + choice)
		if correct == True:
			Question.setAnswer(self, str(self.choiceNum))

	def multiChoices(self):
		for i in self._choice:
			print(i, end=' ')

	def display(self):
		print(self.question)
		if len(self._choice) > 0:
			self.multiChoices()

def main():
	q1 = ChoiceQuestion("In which country was the inventor of Python born?")
	q1.addChoice("Australia", False)
	q1.addChoice("Canada", False)
	q1.addChoice("Netherlands", True)
	q1.addChoice("United States", False)
	q1.display()
	userChoice = str(input("\nPlease select a number: "))
	q1.checkAnswer(userChoice)

	q2 = ChoiceQuestion("What is Python?")
	q2.setAnswer("A programming language")
	q2.display()
	userChoice = input("Please type an answer: ")
	q2.checkAnswer(userChoice)

	q3 = ChoiceQuestion("Why do volcanoes erupt?")
	q3.addChoice("The Earth is angry", False)
	q3.addChoice("Aliens", False)
	q3.addChoice("The Earth is vomiting what it ate for dinner last night", False)
	q3.addChoice("Tectonic plates", True)
	q3.display()
	userChoice = str(input("\nPlease select a number: "))
	q3.checkAnswer(userChoice)

if __name__ == '__main__':
	main()
		

'''
OUTPUT

In which country was the inventor of Python born?
1. Australia 2. Canada 3. Netherlands 4. United States 
Please select a number: 3
Correct!

What is Python?
Please type an answer: Idk lul
Sorry, the answer is:  A programming language

Why do volcanoes erupt?
1. The Earth is angry 2. Aliens 3. The Earth is vomiting what it ate for dinner last night 4. Tectonic plates 
Please select a number: 4
Correct!
'''