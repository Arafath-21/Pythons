import random

def get_choices():
    player_choice = input('Enter a choice(rock,paper,scissors) : ')
    options = ["rock","paper","scissors"]
    computer_choice = random.choice(options)
    choices = {"player":player_choice,"computer":computer_choice}
    return choices

def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    
    if player == computer:
        return "It's a tie!"
    
    # If player chooses rock
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rock! You lose."
    
    # If player chooses paper
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You win!"
        else:
            return "Scissors cut paper! You lose."
    
    # If player chooses scissors
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cut paper! You win!"
        else:
            return "Rock smashes scissors! You lose."
    
    else:
        return "Invalid choice. Please choose 'rock', 'paper', or 'scissors'."

choices = get_choices()
result = check_win(choices["player"],choices["computer"]);
print(result)