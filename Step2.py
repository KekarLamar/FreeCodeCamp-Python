import random

def getChoices():

    player_choice = input ("Enter a choice (rock, paper, scissors: ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice , "computer" : computer_choice}
    return choices

def checkWin (player, computer):
    print ( f"You chose {player} , computer chose {computer}")
    if player == computer:
        return "It's a tie"
    elif player == "rock":
        if computer == "scissors":
            return "Player wins"
        else:
            return "Paper covers rock! You lose."
        
    elif player == "paper":
            if computer == "rock":
                return "Player wins"
            else:
                return "Scissor cuts paper! You lose."

    elif player == "scissors":
                if computer == "paper":
                    return "Player wins"
                else:
                    return "Rock smashes scissors! You lose."

choices = getChoices()
result = checkWin (choices["player"],choices["computer"])
print(result)
print(choices)

