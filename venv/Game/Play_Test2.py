import random

#GLOBAL VARIABLES FOR CHARACTER
list = ['THIEF', 'HERO', 'TANK', 'BERSERKER']

baseStats = [4,4,5,5,3,3,5,5,4,5]

def enemy():
    e_attack = 1
    e_defense = 1
    e_speed = 3
    e_health = 6

def character():
    attack = random.choice(baseStats)

    health = random.choice(baseStats)

    defense = random.choice(baseStats)

    speed = random.choice(baseStats)

    total_stats = attack + defense + speed

    display = 'Title: {}\nStats\nHealth: {}\nAttack: {}\nDefense: {}\nSpeed: {}'.format(title,health, attack, defense, speed)

    print(display)

    print('Total Stats: {}'.format(total_stats))

    if total_stats > 10:
        print('You have some good stats')
    else:
        print('You have bad stats')


#Given choice of a class
for x in list:
    print(x)
adventurer = input('Please choose a class: ')


#REPEATING if input is not in the list
while adventurer.upper() not in list:
    for x in list:
        print(x.upper())
    adventurer = input("That's not a class, please choose one:")

#Determins name for class you chose
if adventurer.upper() in list:
    if adventurer.upper() == list[0]:
        title = adventurer.upper()

    elif adventurer.upper() == list[1]:
        title = adventurer.upper()

    elif adventurer.upper() == list[2]:
        title = adventurer.upper()

    elif adventurer.upper() == list[3]:
        title = adventurer.upper()
    else:
        pass
character()


