# Rules of Rock, Paper, Scissors:
# - Rock beats Scissors (Rock crushes Scissors)
# - Scissors beats Paper (Scissors cut Paper)
# - Paper beats Rock (Paper covers Rock)
# - If both choices are the same, it's a tie

import random

def get_computer_choice():
    """Generate a random choice for the computer"""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_user_choice():
    """Get the user's choice"""
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        user_choice = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()
    return user_choice

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on the rules of Rock, Paper, Scissors"""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    """Simulate a game of Rock, Paper, Scissors"""
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()
