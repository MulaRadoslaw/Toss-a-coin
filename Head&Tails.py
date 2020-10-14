import random

def game():

# greetings
    print("Welcome!")
    print("Throw a coin to win a prize!")

# choice
    while True:
        base_choice = ['Head', 'Tails']
        drawn = random.choice(base_choice)

        user_choice = input('\nHead or Tails? ').capitalize()
        if user_choice in base_choice:
            print(f'You played: {user_choice}')
        elif user_choice == "Exit":
            exit()
        else:
            print("Correctly, please!")
            continue

# rolling
        print(f'\nDrawn: {drawn}\n')


# round winner selection
        computer_wins = 'The computer wins!'
        you_win = 'You win!'

# scoring
        if user_choice == 'Head' and drawn == 'Tails' or \
            user_choice == 'Tails' and drawn == 'Head':
            print(computer_wins)

        elif user_choice == 'Head' and drawn == 'Head' or \
            user_choice == 'Tails' and drawn == 'Tails':
            print(you_win)

game()