import random

lives = 5

animals = ['Shark', 'Cat', 'Dog', 'Fish', 'Snake', 'Horse', 'Squid', 'Cow', 'Chicken', 'Frog', 'Dragon']

animals_str = ', '.join(animals)

answer = str(random.choice(animals))

while 0 < lives <= 5:
    print(answer.lower())
    print('You have ' + str(lives) + ' lives.')
    guess = input('\n' + animals_str + "\n\nGuess the animal: ")

    while guess.lower() not in animals_str.lower():
        guess = input('Your animal in not on the list, please guess again: ')


    if guess.lower() != answer.lower():
        print("\nOops, you guessed the wrong animal! You lose a life.")
        lives = lives - 1

    elif guess.lower() == answer.lower():
        print("YOU WIN")
        break

else:
    print('\nYou have no lives remaining. YOU LOSE')