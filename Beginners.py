import random

def get_choices():

    player_choice = input ("Enter a choice (rock, paper, scissors: ")
    options = ["rock", "paper", "scissors"]
    computer_choice = "rock"
    choices = {"Player": player_choice , "Computer" : computer_choice}
    return choices

choices = get_choices()

print (choices)
