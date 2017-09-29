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

while (repeat == True): # while loop for continuous games
    userChoice = input("Enter 'rock', 'paper', 'scissors', or 'exit' to quit: ")
    userChoice = userChoice.lower() # user input lowercased
    compChoice = random.choice(["rock","paper","scissors"]) # random choice by computer
    print("You chose:", userChoice, " Computer chose:", compChoice)
    if (userChoice == compChoice): # both choices are the same
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
    elif (userChoice == "exit"): # exits loop, displays scores
        print("Final scores: User:", userWin, " Computer:", compWin, " Tie:", tie)
        repeat = False
    else:
        print("Please enter a valid choice!")
print("Thanks for playing!")

'''
test results for BMI calculator

Please enter a weight in pounds: 160
Please enter a height in inches: 60
Your BMI is: 31.2
You are obese.

Please enter a weight in pounds: 160
Please enter a height in inches: 65
Your BMI is: 26.6
You are overweight.

Please enter a weight in pounds: 160
Please enter a height in inches: 70
Your BMI is: 23.0
You are normal.

Please enter a weight in pounds: 160
Please enter a height in inches: 80
Your BMI is: 17.6
You are underweight.

test results for rock paper scissors game

Rock-Paper-Scissors Game!
Enter 'rock', 'paper', 'scissors', or 'exit' to quit: rock
You chose: rock  Computer chose: rock
It's a tie!
Enter 'rock', 'paper', 'scissors', or 'exit' to quit: rock
You chose: rock  Computer chose: scissors
You win! Rock beats scissors!
Enter 'rock', 'paper', 'scissors', or 'exit' to quit: paper
You chose: paper  Computer chose: paper
It's a tie!
Enter 'rock', 'paper', 'scissors', or 'exit' to quit: scissors
You chose: scissors  Computer chose: rock
You lose! Rock beats scissors!
Enter 'rock', 'paper', 'scissors', or 'exit' to quit: paper
You chose: paper  Computer chose: rock
You win! Paper beats rock!
Enter 'rock', 'paper', 'scissors', or 'exit' to quit: rock
You chose: rock  Computer chose: scissors
You win! Rock beats scissors!
Enter 'rock', 'paper', 'scissors', or 'exit' to quit: exit
You chose: exit  Computer chose: paper
Final scores: User: 3  Computer: 1  Tie: 2
Thanks for playing!
'''
