import random
import sys
import time
import os
### DEFINES ADVENTURER ###

class Adventurer:
    def __init__(stat, title, health, attack, defense, speed):
        stat.title = title
        stat.health = health
        stat.attack = attack
        stat.defense = defense
        stat.speed = speed

class enemy:
    def __init__(e_stat, e_health, e_attack, e_defense, e_speed):
        e_stat.e_health = e_health
        e_stat.e_attack = e_attack
        e_stat.e_defense = e_defense
        e_stat.e_speed = e_speed

### PLAYER'S HUD ###

def char_display():

    display = ('\nTitle: {}\nHP: {} ATK: {} DEF: {} SPD: {}'.format(player.title,player.health,player.attack,player.defense,player.speed))
    print(display)

### ENEMIES HUD ###

def enemy_display():

    e_display = '\nENEMY STATS\nHP: {} ATK: {} DEF: {}\n'.format(enemy1.e_health,enemy1.e_attack,enemy1.e_defense)
    print(e_display)

### FUNCTION FOR WHEN THE PLAYER DEALS DAMAGE ###
def damage_dealt():
    dealt = player.attack - enemy1.e_defense

    if dealt <= 0:
        damage = ('\nThe enemy takes 1 damage')
        for character in damage:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.2)
        enemy1.e_health = enemy1.e_health-1

    else:
        damage2 = ('\nYou deal {} damage'.format(dealt))
        for character in damage2:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.2)
        enemy1.e_health = enemy1.e_health - dealt

### FUNCTION FOR THE DAMAGE THE PLAYER RECEIVES ###

def damage_receive():
    receive = enemy1.e_attack - player.defense

    if receive <= 0:
        damage = ('\nYou take 1 damage')
        for character in damage:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.2)
        player.health = player.health -1

    else:
        damage2 = ('You take {} damage\n'.format(receive))
        for character in damage2:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.15)
        player.health = player.health - receive


### BATTLE SEQUENCE ###

def battle():
    while player.health > 0 and enemy1.e_health > 0:
        char_display()
        enemy_display()

        action_list = ['ATTACK', 'PASS']
        for x2 in action_list:
            print('>' + x2)
        action = input("What will you do? ")

        if action.upper() == 'ATTACK':
            damage_dealt()
            damage_receive()

        else:
            pass


### INTRO TEXT ###


def intro_text():
    name = input('What is your name adventurer? ')
    print('{}, what a wonderful name!'.format(name))
    time.sleep(1)
    print('You\'ve been summoned into the world of Fravilion, a world full of magic!')
    time.sleep(1)
    print('Let\'s make sure you choose a class before you set out on your quest')
    time.sleep(1)
    print('Please, choose a class')
    time.sleep(1)



enemystat = [2,3]
basestats = [4,4,4,3,3]
char_list = ['THIEF', 'HERO', 'TANK', 'BERSERKER']

### ACTUAL CODE ###

intro_text()


for x in char_list:
    print(x)

adventurer = input('Please choose a class: ')

#### Determins name for class you chose ###

if adventurer.upper() not in char_list:
    while adventurer.upper() not in char_list:
        for x in char_list:
            print(x.upper())

        adventurer = input("That's not a class, please choose one:")
        title = adventurer.upper()
else:
    title = adventurer.upper()

### REPEATING if input is not in the list ###



### PLAYER AND ENEMIES ###

player = Adventurer(title.upper(),random.choice(basestats),random.choice(basestats),random.choice(basestats),random.choice(basestats))

enemy1 = enemy(random.randint(4,5),random.choice(enemystat),random.choice(enemystat),random.choice(enemystat))

battle()