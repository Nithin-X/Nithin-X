import random
print("Welcome to my Rock!...Paper!...Scissor!...GAME by Nithin-x")
user_wins=0
computer_wins=0

objects=["rock","paper","scissors"]


while True:
    inp=input("Type Rock/Paper/Scissors else q for quit the game :")

    if inp.lower()=="q":
        print("See you next time Goodbye!....")
        break
    
    if inp.lower() not in objects:
        print("please enter a valid code!....")
        continue
    random_no=random.randint(0,2)

    computer_choice= objects[random_no]
    
    if inp == "rock" and computer_choice=="scissors":
        print("User wins!...")
        user_wins +=1

    elif inp == "paper" and computer_choice=="rock":
        print("User wins!...")
        user_wins +=1
    

    elif inp == "scissors" and computer_choice=="paper":
        print("User wins!...")
        user_wins +=1
    else:
        print("you lost computer wins!...")
        computer_wins+=1
    
print("total games user wins ",user_wins)
print("total games computer wins",computer_wins)





