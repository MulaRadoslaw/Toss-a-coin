import time
import random

def game():

# greetings
    print("Welcome!")
    time.sleep(1)
    print("Throw a coin to win a prize!")

# points
    computer_count = 0
    user_count = 0

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
        print("\nThrowing...")
        time.sleep(1)
        print(f'Drawn: {drawn}\n')

# round winner selection
        computer_wins = 'The computer wins!'
        you_win = 'You win!'

# scoring
        if user_choice == 'Head' and drawn == 'Tails' or \
            user_choice == 'Tails' and drawn == 'Head':
            print(computer_wins)

            computer_count += 1

        elif user_choice == 'Head' and drawn == 'Head' or \
            user_choice == 'Tails' and drawn == 'Tails':
            print(you_win)

            user_count += 1

        print(f'Computer: {computer_count} - You: {user_count}')

# winner selection
        if user_count == 3 :
            print("Player is a WINNER")
            break
        elif computer_count == 3:
            print('Computer is a WINNER')
            break

game()
input()
