import random
'''
weight = float(input("Please enter a weight in pounds: "))
height = float(input("Please enter a height in inches: "))
bmi = round(weight / height**2 * 703, 1)
print("Your BMI is:", bmi)
if (bmi < 18.5):
    print("You are underweight.")
elif (bmi <= 24.9):
    print("You are normal.")
elif (bmi <= 29.9):
    print("You are overweight.")
else:
    print("You are obese.")
'''
print("Rock-Paper-Scissors Game!")
userWin = 0
compWin = 0
tie = 0
userChoice = input("Enter 'rock', 'paper', 'scissors', or 'exit' to quit: ")
userChoice = userChoice.lower()
while (userChoice != "exit"):
    if (userChoice != "rock" or userChoice != "paper" or userChoice != "scissors" or userChoice != "quit"):
        print("Fail")
        while (userChoice != "rock" or userChoice != "paper" or userChoice != "scissors"):
            userChoice = input("Enter 'rock', 'paper', 'scissors', or 'exit' to quit: ")
            userChoice = userChoice.lower()
            if (userChoice == "quit"):
                break
            else:
                compChoice = random.choice(["rock","paper","scissors"])
                print("User choice is:", userChoice)
                print("Computer choice is:", compChoice)

else:
    print("Thanks for playing!")


