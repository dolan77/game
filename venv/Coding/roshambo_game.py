# import random
#
# def action():
#     options = ['rock' , 'paper' , 'scissors']
#     player_choice = input('Please choose rock / paper / scissors :').lower()
#
#     while player_choice not in options:
#         player_choice = input('INVALID INPUT: Please choose rock / paper / scissors :').lower()
#
#     bot_choice = random.choice(options)
#     print('You chose {} and the CPU chose {}'.format(player_choice.upper(),bot_choice.upper()))
#     print(game(player_choice , bot_choice))
#
# def game(x , y):
#
#     if x == 'rock' and y == 'scissors':
#         winner = 'Player wins'
#         return winner
#
#     if x == 'paper' and y == 'rock':
#         winner = 'Player wins'
#         return winner
#
#     if x == 'scissors' and y == 'paper':
#         winner = 'CPU wins'
#         return winner
#
#     if x == 'rock' and y == 'paper':
#         winner = 'CPU wins'
#         return winner
#
#     if x == 'paper' and y == 'scissors':
#         winner = 'CPU wins'
#         return winner
#
#     if x == 'scissors' and y == 'rock':
#         winner = 'CPU wins'
#         return winner
#
#     else:
#         winner = "DRAW"
#         return winner
#
# action()