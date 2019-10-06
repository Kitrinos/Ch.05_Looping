'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''
#Var
miles = 0
birds = 3
quit = "no"
ag = 10

#The title
string = " Mortal Misadventure"

new_string = string.center(130)

print("\n", new_string)

#Instructions

while x.lower() != "yes" or x.lower() != "y":
    x = input("Do you want to quit? ")
    if x.lower() == "yes" or x.lower() == "y":
        print("You quit")

    elif quit.lower() == "no" or quit.lower() == "n":
        an = input("\nWould you like instructions?\n")

        if an.lower() == "yes" or an.lower() == "y":
            print("\nThe object of the game is to travel 200 miles across Illia to find Illias hidden treasure.")
            print("You are a beginning adventure, wanting to find the legendary treasure.")
            print("A Guild of angry warriors will be chasing you along the journey. You will be asked for commands every so often.")
            print("\nC O M M A N D S:")
            print("Talk to Camel | Drink water | Quit | Status check | Full speed | Normal speed | Stop | Eat a bird\n")
            print("You have three birds to start the game which will last you six days. You may renew your birds at rest stops along your journey.")
            print("Good luck and Good Adventuring!!")
        else:
            print("sorry try again")

#Game Start

print("\nYou are in a small town 200 miles away from the temple.")
while done == False:
    print("\nYou have traveled", miles, "altogether\n")
    print("What is your command")
    an = input("Quit | Status check | Full speed | Normal speed | Stop | Eat a bird\n")

    if an.lower() == "status check":
        print("Miles traveled :", miles)
        print("Birds :",birds)
        print("The Angry Guild is",ag ," miles behind you")
    elif an.lower() == "quit":
        print("You Quit")
   
#everything after the status check does not work
        
# print("\nYou are in a small town 200 miles away from the temple.")
# while done == False:
#     print("\nYou have traveled", miles, "altogether\n")
#     print("What is your command")
#     an = input("Quit | Status check | Full speed | Normal speed | Stop | Eat a bird \n")

    
#     if an.lower() == "quit":
#         print("You quit")
#     elif an.lower() == "status check":
#         print("Miles traveled :", miles)
#         print("Birds :",birds)
#         print("The Angry Guild is",ag ," miles behind you")
#     elif an.lower == "full speed":
#         print("Full speed ahead.")
#         print("Becarefull of your camel, they might get tired")
#     elif an.lower == "normal speed":
#         print("Your camel thanks you! Normal speed ahead")
#     elif an.lower == "Stop":
#         print("You decided to stop. But dont stop for too long, you might just get lost....")
#     elif an.lower() == "eat a bird":
#         print("You eat a bird")
#         birds-= 1
#         print("becarefull not to run out of birds. You have", birds, "left")
#     else:
#         print("That is not a option. Please try again before you die :)") 
