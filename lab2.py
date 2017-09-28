import random

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

print("Rock-Paper-Scissors Game!")
userWin = 0 # keeps track of scores
compWin = 0
tie = 0
repeat = True # keeps game going

while (repeat == True):
    userChoice = input("Enter 'rock', 'paper', 'scissors', or 'exit' to quit: ")
    userChoice = userChoice.lower()
    compChoice = random.choice(["rock","paper","scissors"])
    print("You chose:", userChoice, " Computer chose:", compChoice)
    if (userChoice == compChoice):
        print("It's a tie!")
        tie += 1
    elif (userChoice == "rock"):
        if (compChoice == "scissors"):
            print("You win! Rock beats scissors!")
            userWin += 1
        else:
            print("You lose! Paper beats rock!")
            compWin += 1
    elif (userChoice == "paper"):
        if (compChoice == "rock"):
            print("You win! Paper beats rock!")
            userWin += 1
        else:
            print("You lose! Scissors beats paper!")
            compWin += 1
    elif (userChoice == "scissors"):
        if (compChoice == "paper"):
            print("You win! Scissors beats paper!")
            userWin += 1
        else:
            print("You lose! Rock beats scissors!")
            compWin += 1
    elif (userChoice == "exit"):
        print("Final scores: User:", userWin, " Computer:", compWin, " Tie:", tie)
        repeat = False
    else:
        print("Please enter a valid choice!")
print("Thanks for playing!")


