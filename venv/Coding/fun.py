#state = 'Cali'

#state2 = 'helo'

#state3 = 'dumb'

#print(state, state2, state3 )
#print(state, state2, state3, sep= ';;', end = '.')


#print("test")


#yeet= "hello"

#print ("sup, %s" % yeet )

#print(format(0.2, '.0%'))

import random

animals = ['Pig' , 'cat', 'dog']

animals_str = ', '.join(animals)

answer = random.choice(animals)
lives = 5

while 0 < lives <= 5:
    print('You have ' + str(lives) + ' lives.')

    print(answer)

    guess = input('\n' + animals_str + "\n\nGuess the animal: ")

    if guess in animals_str:

        if guess != answer:
             print("\nOops, you guessed the wrong animal! You lose a life.")
             lives -= 1


        elif guess == answer:
            print('YOU WIN')
            break
    else:
        guess = input("Guess the animal again: ")




else:
    print("YOU LOSE")