import random

def dice():
    roll_1 = random.randrange(1,7)

    roll_2 = random.randrange(1,7)

    return roll_1 , roll_2

answer = ['yes' , 'no']

question = input('Would you like to roll the dice? yes / no : ')

i = True

while question not in answer:

    question = input('Please input a valid answer. yes / no : ')

while question in answer and i is True:

    if question == 'yes':
        roll = dice()

        print('\nYou rolled {} and {}'.format(roll[0], roll[1]))

        question = input('Would you like to roll again? yes / no :')

    else:
        i = False

else:
    print('Okay, have a nice day!')
