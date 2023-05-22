import random
from colorama import Fore, Back
rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'

score_player = 0
while True:
    player_move = input("Choose [r]ock, [p]aper, [s]cissors :")

    if player_move == 'r':
        player_move = rock
    elif player_move == 'p':
        player_move = paper
    elif player_move == 's':
        player_move = scissors
    else:
        print('Invalid input. Try again...')
        continue

    computer_random_number = random.randint(1, 3)

    computer_move = ''

    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    elif computer_random_number == 3:
        computer_move = scissors

    if (player_move == rock and computer_move == scissors) or (player_move == paper and computer_move == rock)\
            or (player_move == scissors and computer_move == paper):
        score_player += 1
        print(Fore.RED + 'Yuo win!')
    elif (player_move == scissors and computer_move == rock) or (player_move == rock and computer_move == paper)\
            or (player_move == paper and computer_move == scissors):
        score_player -= 1
        print(Fore.GREEN + 'Yuo lose!')
    else:
        print(Fore.BLUE + 'Draw!')
    command = input('Type [y] to play or [n] to quit :')
    if command == 'n':
        print('Tank to playing!')
        break
if score_player < 0:
    print('You score = 0')
else:
    print(f'You score = {score_player}')




