'''
ROSHAMBO PROGRAM
----------------

Create a program that randomly prints 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.
(It will be easier if you have them enter 1 for rock, 2 for paper, and 3 for scissors.)
Add conditional statements to figure out who wins and keep the records
When the user quits print a win/loss record

'''
import random
u = 0
quit = "no"

i = random.randrange(3)

if i == 1:
  print("rock")
elif i == 2:
  print("paper")
else:
  print("scissors")

while quit.lower() != "yes" or quit.lower() != "y":
    b = random.randrange(3)+1
    quit = input("Do you want to quit? ")
    if quit.lower() == "yes" or quit.lower() == "y":
        print("You quit")
    elif quit.lower() == "no" or quit.lower() == "n":
        u = input("Hello user! What is your choice? (rock, paper, scissors) ")

        if b == 1:
            print("rock")
        elif b == 2:
            print("paper")
        else:
            print("scissors")

        if b == 1:
            if u.lower() == "rock":
                print("The bot chose rock! You tie!")

        if b == 1:
            if u.lower() == "paper":
                print("The bot chose rock! You Win!")

        if b == 1:
            if u.lower() == "scissors":
                print("The bot chose rock! You lose!")

        if b == 2:
            if u.lower() == "paper":
                print("The bot chose paper! You got a tie!")

        if b == 2:
            if u.lower() == "rock":
                print("The bot chose paper! You lose!")

        if b == 2:
            if u.lower() == "scissors":
                print("The bot chose paper! You Win!")

        if b == 3:
            if u.lower() == "scissors":
                print("The bot chose scissors! You tie!")

        if b == 3:
            if u.lower() == "rock":
                print("The bot chose scissors! You Win!")

        if b == 3:
            if u.lower() == "paper":
                print("The bot chose scissors! You lose!")
    else:
        print("sorry try again")
