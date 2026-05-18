player1 = (input("Player 1: Enter your choice:").capitalize())
player2 = (input("Player 2: Enter your choice:").capitalize())

if player1 == player2:
    print("Tie")

else:

    if player1 == "Rock":
        if player2 == "Paper":
            print("player 2 Wins!")
        else:
            print("Player 1 Wins!") 
    
    elif player1 == "Paper":
        if player2 == "Scissors":
            print("Player 2 Wins!")
        else:
            print("Player 1 Wins")

    elif player1 == "Scissors":
        if player2 == "Rock":
            print("Player 2 Wins!")
        else:
            print("Player 1 Wins!")

    else:
        print("invalid choice")        
