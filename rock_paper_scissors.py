import random

while True:
    choices = ["rock","paper","scissors"]

    computer = random.choice(choices)
    player= None
    
    while player not in choices:
        player= input("rock, paper or scissors?: ").lower()

    if player == computer: 
        print("computer: ",computer)
        print("player: ",player)
        print("tie!!")
        
    elif player == "rock":
        if computer == "paper":
            print("computer: ",computer)
            print("player: ",player)
            print("U Lose :(")
        if computer == "scissors":
            print("computer: ",computer)
            print("player: ",player)
            print("U Win :)")
            
    elif player == "scissors":
        if computer == "rock":
            print("computer: ",computer)
            print("player: ",player)
            print("U Lose :(")
        if computer == "paper":
            print("computer: ",computer)
            print("player: ",player)
            print("U Win :)")
            
    elif player == "paper":
        if computer == "scissors":
            print("computer: ",computer)
            print("player: ",player)
            print("U Lose :(")
        if computer == "rock":
            print("computer: ",computer)
            print("player: ",player)
            print("U Win :)")

    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":      
        break
print("Bye!")


        
