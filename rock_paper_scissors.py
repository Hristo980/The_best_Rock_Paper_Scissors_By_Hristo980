import random
from colorama import Fore, Back, Style

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'
wins_counter = 0
lose_counter = 0

while wins_counter < 2 or lose_counter < 2:

    player_move = input(Fore.BLACK + 'Chose [r]ock, [p]aper or [s]cissors: ')

    if player_move.lower() == 'r':
        player_move = rock
    elif player_move.lower() == 'p':
        player_move = paper
    elif player_move.lower() == 's':
        player_move = scissors
    else:
        print('Invalid Input. Try again...')

    computer_random_number = random.randint(1, 3)
    computer_random_move = ''

    if computer_random_number == 1:
        computer_random_move = rock
    elif computer_random_number == 2:
        computer_random_move = paper
    elif computer_random_number == 3:
        computer_random_move = scissors

    print(Fore.BLUE + f'The computer chose {computer_random_move}.')

    if (player_move == rock and computer_random_move == scissors) or \
            (player_move == paper and computer_random_move == rock) or \
            (player_move == scissors and computer_random_move == paper):
        print(Fore.GREEN + 'You win!')
        wins_counter += 1
        if wins_counter >= 2:
            wins_counter = 0
            print(Fore.GREEN + 'Final result: You are the big winner!')
            one_more_game = input(Fore.CYAN + 'Type [y] to Play Again or [n] to quit: ')
            if one_more_game.lower() == 'y':
                wins_counter = 0
                continue
            elif one_more_game.lower() == 'n':
                print(Fore.CYAN + 'Thank you for playing with us!')
                break
    elif player_move == computer_random_move:
        print(Fore.YELLOW + 'Draw!')

    else:
        print(Fore.RED + 'You lose!')
        lose_counter += 1
        if lose_counter >= 2:
            lose_counter = 0
            print(Fore.RED + 'Final result: The computer is the big winner!')
            one_more_game = input(Fore.CYAN + 'Type [y] to Play Again or [n] to quit: ')
            if one_more_game.lower() == 'y':
                lose_counter = 0
                continue
            elif one_more_game.lower() == 'n':
                print(Fore.CYAN + 'Thank you for playing with us!')
                break
