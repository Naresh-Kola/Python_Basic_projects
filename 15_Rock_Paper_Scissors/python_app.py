import random 

exit = False
user_points = 0
computer_points = 0

while exit == False:
    options = ["rock", "paper", "scissors"]
    user_input = input("Choose rock, paper, scissors or exit: ")
    computer_input = random.choice(options)

    if user_input == "exit":
        print("Game ended")
        exit = True 
   
    elif user_input == "rock":
        if computer_input == "rock":
            print("User input rock")
            print("computer input is rock")
            print("Its a Tie")
        elif computer_input == "paper":
            print("User input rock")
            print("Computer input paper")
            print("Computer wins")
            computer_points += 1
        else:
            print("User input rock")
            print("Computer input scissor")
            print("You Win")
            user_points += 1
    elif user_input == "paper":
        if computer_input == "rock":
            print("User input paper")
            print("Computer input rock")
            print("You Win")
            user_points += 1
        elif computer_input == "paper":
            print("User input paper")
            print("Computer input paper")
            print("Its Tie")
        else:
            print("User input paper")
            print("Computer input scissor")
            print("Computer Wins")
            computer_points += 1
    elif user_input == "scissors":
        if computer_input == "rock":
            print("User input scissor")
            print("Computer input rock")
            print("You Win")
            user_points += 1
        elif computer_input == "paper":
            print("User input scissor")
            print("Computer input paper")
            print("Computer Wins")
            computer_points += 1
        else:
            print("User input scissor")
            print("Computer input scissor")
            print("Its Tie")
    else:
        print("Invalid Input")


print("User Points: ", user_points)
print("Computer points: ",computer_points)
                



