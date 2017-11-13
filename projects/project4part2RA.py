

class Question:

	def __init__(self):
		self.question = ""
		self.answer = ""

	def setText(self, questionText):
		self.question = questionText

	def setAnswer(self, correctResponse):
		self.answer = correctResponse

	#new
	def getAnswer(self):
		return self.answer

	def checkAnswer(self, response):
		return self.answer == response
		

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

	def singleAnswer(self, answer):
		Question.setAnswer(self, answer)

def main():
	q1 = ChoiceQuestion("In which country was the inventor of Python born?")
	q1.addChoice("Australia", False)
	q1.addChoice("Canada", False)
	q1.addChoice("Netherlands", True)
	q1.addChoice("United States", False)
	q1.display()
	q1.multiChoices()
	userChoice = str(input("\nPlease select a number: "))
	if q1.checkAnswer(userChoice):
		print("Correct!")
	else:
		print("Sorry, the answer is: " + q1.getAnswer())
	print("")

	q2 = ChoiceQuestion("What is Python?")
	q2.singleAnswer("A programming language")
	q2.display()
	userChoice = input("Please type an answer: ")
	if q2.checkAnswer(userChoice):
		print("Correct!")
	else:
		print("Sorry, the answer is: " + q2.getAnswer()) 
	print("")

	q3 = ChoiceQuestion("Why do volcanoes erupt?")
	q3.addChoice("The Earth is angry", False)
	q3.addChoice("God is angry", False)
	q3.addChoice("The Earth is vomiting what it ate for dinner last night", False)
	q3.addChoice("Tectonic plates", True)
	q3.display()
	q3.multiChoices()
	userChoice = str(input("\nPlease select a number: "))
	if q3.checkAnswer(userChoice):
		print("Correct!")
	else:
		print("Sorry, the answer is: " + q1.getAnswer())
	print("")


if __name__ == '__main__':
	main()
		
