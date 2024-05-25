import random

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'

player_move = input('Chose [r]ock, [p]aper or [s]cissors: ')

if player_move == 'r':
    player_move = rock
elif player_move == 'p':
    player_move = paper
elif player_move == 's':
    player_move = scissors
else:
    raise SystemExit('Invalid Input. Try again...')

computer_random_number = random.randint(1, 3)
computer_random_move = ''

if computer_random_number == 1:
    computer_random_move = rock
elif computer_random_number == 2:
    computer_random_move = paper
elif computer_random_number == 3:
    computer_random_move = scissors

print(f'The computer chose {computer_random_move}.')

if (player_move == rock and computer_random_move == scissors) or \
        (player_move == paper and computer_random_move == rock) or \
        (player_move == scissors and computer_random_move == paper):
    print('You win!')
elif player_move == computer_random_move:
    print('Draw!')
else:
    print('You lose!')