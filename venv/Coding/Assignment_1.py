import random


animal = int(input("Choose an integer between 1-8: "))

while animal < 1:

    animal = int(input("Please choose an integer between 1-8: "))

while animal > 8:
    animal = int(input("Please choose an integer between 1-8: "))

if 1 <= animal <= 8:
    lives = 5

else:
    pass

#Will determing what animal you need to guess based on the number chosen
if animal == 1:
     string1 = "dog"

elif animal == 2:
    string1 = "cat"

elif animal == 3:
    string1 = "fish"

elif animal == 4:
    string1 = "snake"

elif animal == 5:
    string1 = "shark"

elif animal == 6:
    string1 = "horse"

elif animal == 7:
    string1 = "squid"

elif animal == 8:
    string1 = "cow"

#The Actual Guessing Game \/ \/
while 0 < lives <= 5:
    list = 'shark' , 'fish' , 'dog' , 'snake' , 'horse' , 'cow' , 'cat' , 'squid'
    string2 = input("You have {} lives\n\n".format(lives) + str(list) + "\n\nPlease guess the animal (Don't add '' to your answer) : ")

    if string1 != string2:
        print("\nOops, that's the wrong animal! You lose a life\n")
        lives = lives - 1

    elif string1 == string2:
        print("\n Yay, you got it right! \n\t\tYOU WIN")
        break

if lives == 0:
    print("\nYou ran out of lives. \n\t\tYOU LOSE")
