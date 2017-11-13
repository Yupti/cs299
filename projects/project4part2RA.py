

class Question:

	def __init__(self):
		self.question = ""
		self.answer = ""

	def setText(self, questionText):
		self.question = questionText

	def setAnswer(self, correctResponse):
		self.answer = correctResponse

	def checkAnswer(self, response):
		if self.answer == response:
			print("Correct!")
		else:
			print("Incorrect...")

	def display(self):
		print(self.question)

class ChoiceQuestion(Question):

	def __init__(self):
		print("IDK YET")

	def addChoice(self, choice, correct):
		
