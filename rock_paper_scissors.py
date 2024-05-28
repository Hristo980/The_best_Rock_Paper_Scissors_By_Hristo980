import random
from colorama import Fore, Back, Style

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'
wins_counter = 0
lose_counter = 0
wins_counter_for_current_result = 0
lose_counter_for_current_result = 0

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

    if (player_move == rock and computer_random_move == scissors) or \
            (player_move == paper and computer_random_move == rock) or \
            (player_move == scissors and computer_random_move == paper):
        wins_counter_for_current_result += 1
        print(Fore.GREEN + f'The computer chose {computer_random_move} and your {player_move} beats it! You win!')
        print(Fore.GREEN + f'Current result {wins_counter_for_current_result}:{lose_counter_for_current_result}')
        wins_counter += 1
        if wins_counter >= 2:
            wins_counter_for_current_result = 0
            lose_counter_for_current_result = 0
            wins_counter = 0
            lose_counter = 0
            print(Fore.GREEN + 'Final result: You are the big winner! :)')
            one_more_game = input(Fore.BLACK + 'Type [y] to Play Again or [n] to quit: ')
            if one_more_game.lower() == 'y':
                continue
            elif one_more_game.lower() == 'n':
                print(Fore.BLACK + 'Thank you for playing with us, you smashed the computer!')
                break
    elif player_move == computer_random_move:
        wins_counter_for_current_result += 1
        lose_counter_for_current_result += 1
        print(Fore.YELLOW + f'The computer chose {computer_random_move} which is equal to your {player_move}! Draw!')
        print(Fore.YELLOW + f'Current result {wins_counter_for_current_result}:{lose_counter_for_current_result}')
    else:
        lose_counter_for_current_result += 1
        print(Fore.RED + f'The computer chose {computer_random_move} which beats your {player_move}! You lose!')
        print(Fore.RED + f'Current result {wins_counter_for_current_result}:{lose_counter_for_current_result}')
        lose_counter += 1
        if lose_counter >= 2:
            wins_counter_for_current_result = 0
            lose_counter_for_current_result = 0
            wins_counter = 0
            lose_counter = 0
            print(Fore.RED + 'Final result: The computer is the big winner! :(')
            one_more_game = input(Fore.BLACK + 'Type [y] to Play Again or [n] to quit: ')
            if one_more_game.lower() == 'y':
                continue
            elif one_more_game.lower() == 'n':
                print(Fore.BLACK + "Thank you for playing with us and please don't give up, it's just a game!")
                break
