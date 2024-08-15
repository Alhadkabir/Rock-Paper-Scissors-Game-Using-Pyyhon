import random

possible_actions = ["rock", "paper", "scissors"]

def take_user_input():

    try:
        user_input = int(input("""Which one will you choose?
1. Rock
2. Paper
3. Scissors
: """))
    except ValueError:
        print("Invalid input. Please enter a number given above.")
        return

    if user_input > len(possible_actions) or user_input < 0:
        print("Invalid input. Number is outside range of 1-3")
        return

    user_action = possible_actions[user_input - 1]

    return user_action

def determine_winner(user_action, computer_action):

    if user_action == computer_action:
        print("Both computer and user has selected " + user_action + ". It's a tie.")
        return

    match user_action:
        case "rock":
            if computer_action == "paper":
                print("Computer selected paper. Computer wins.")
            else:
                print("Computer selected scissors. User wins.")
        case "paper":
            if computer_action == "rock":
                print("Computer selected rock. User wins.")
            else:
                print("Computer selected scissors. Computer wins.")
        case "scissors":
            if computer_action == "paper":
                print("Computer selected paper. User wins.")
            else:
                print("Computer selected rock. Computer wins.")
        case _:
            print("Default case")

def play_game():
    user_action = take_user_input()
    if user_action == None:
        return

    computer_action = random.choice(possible_actions)
    print("User selected " + user_action)
    return determine_winner(user_action, computer_action)



def main():
    try:
        while True:
            print("Welcome to rock paper scissors game")
            play_game()
            print("")
    except KeyboardInterrupt:
        return print("Bye! Thank you for playing")


main()