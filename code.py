1
import random
# Print game rules
print('Winning rules of the game ROCK PAPER SCISSORS are:\n'
+ "Rock vs Paper -> Paper wins \n"
+ "Rock vs Scissors -> Rock wins \n"
+ "Paper vs Scissors -> Scissors wins \n")
while True:
    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")
    # TODO: Get and convert user input
    # HINT: Use input() to read from the user and wrap it with int()
    choice = int(input())
    # TODO: Keep asking until the input is valid (between 1 and 3)
    # HINT: Use a while loop to check if choice is not in the valid range
    while choice < 1 and choice > 3:
        choice = int(input("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n"))
    # TODO: Map the user’s choice to its name
    # HINT: Use if-elif-else to assign choice_name based on choice number
    if choice == 1:
        choice_name = 'Rock' # HINT: This should be "Rock"
    elif 2:
        choice_name = 'Paper' # HINT: This should be "Paper"
    else:
        choice_name = 'Scissors' # HINT: This should be "Scissors"
    print('User choice is:', choice_name)
    print("Now it's Computer's Turn...")
    # TODO: Computer makes a random choice
    # HINT: Use random.randint() with range 1 to 3
    comp_choice = random.randint(1, 3)
    # TODO: Map computer's choice to its name
    if  comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'
    print("Computer choice is:", comp_choice_name)
    print(choice_name, 'vs', comp_choice_name)
    # TODO: Determine the winner
    # HINT: First handle tie, then combinations where Paper, Rock, or
    #Scissors win
    if choice == comp_choice:
        result = "DRAW"
    elif (choice ==  2 and comp_choice == 3) or (choice == 3 and comp_choice == 2):
        result = 'Paper Wins' # HINT: Paper wins in this case
    elif (choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 1):
        result = 'Rock Wins' # HINT: Rock wins in this case2

    elif (choice == 3 and comp_choice == 2) or (choice == 2 and comp_choice == 3):
        result = 'Scissors win' # HINT: Scissors wins in this case
    # TODO: Print game result
    # HINT: Compare result with "DRAW" and with user choice_name
    if result == "DRAW":
        print("<== It's a tie! ==>")
    elif ((choice == 3 and comp_choice ==2) or (choice == 2 and comp_choice ==1) or (choice == 3 and comp_choice == 2)):
        print("<== User wins! ==>")
    else:
        print("<== Computer wins! ==>")
    # TODO: Ask to play again
    # HINT: Use input() and convert to lowercase
    print("Do you want to play again? (Y/N)")
    ans = input().lower()
    if ans == 'n':
        break
print("Thanks for playing!")