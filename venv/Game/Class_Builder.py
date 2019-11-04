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


### FUNCTION FOR WHEN THE PLAYER DEALS DAMAGE ###
def damage_dealt():
    dealt = player.attack - slime.e_defense

    if dealt <= 0:
        damage = ('\nThe enemy takes 1 damage')
        for character in damage:
            sys.stdout.write(character)
            sys.stdout.flush()
        slime.e_health = slime.e_health-1

    else:
        damage2 = ('\nYou deal {} damage'.format(dealt))
        for character in damage2:
            sys.stdout.write(character)
            sys.stdout.flush()
        slime.e_health = slime.e_health - dealt

### FUNCTION FOR THE DAMAGE THE PLAYER RECEIVES ###

def damage_receive():
    receive = slime.e_attack - player.defense

    if receive <= 0:
        damage = ('\nYou take 1 damage')
        for character in damage:
            sys.stdout.write(character)
            sys.stdout.flush()
        player.health = player.health -1

    else:
        damage2 = ('You take {} damage\n'.format(receive))
        for character in damage2:
            sys.stdout.write(character)
            sys.stdout.flush()
        player.health = player.health - receive


### BATTLE SEQUENCE ###

def battle():
    while player.health > 0 and slime.e_health > 0:
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

### INTRO BATTLE SCENE

def intro_battle():
    print('So you chose to be a {}, excellent choice my friend!'.format(player.title))
    time.sleep(2)
    print('Let us test your combat abilities against this slime!')
    time.sleep(2)
    battle()

### GLOBAL VARIABLES ###


enemystat = [2,3]
char_list = ['THIEF', 'HERO', 'TANK', 'BERSERKER']


### PLAYER AND ENEMIES ###
player = Adventurer('Class',5,4,4,4)
slime = enemy(random.randint(4,5),random.choice(enemystat),random.choice(enemystat),random.choice(enemystat))


### PLAYER'S HUD ###

def char_display():

    display = ('\nTitle: {}\nHP: {} ATK: {} DEF: {} SPD: {}'.format(player.title,player.health,player.attack,player.defense,player.speed))
    print(display)

### ENEMIES HUD ###

def enemy_display():

    e_display = '\nENEMY STATS\nHP: {} ATK: {} DEF: {}\n'.format(slime.e_health,slime.e_attack,slime.e_defense)
    print(e_display)

### PLAYER'S HUD ###

def char_display():

    display = ('\nTitle: {}\nHP: {} ATK: {} DEF: {} SPD: {}'.format(player.title,player.health,player.attack,player.defense,player.speed))
    print(display)

### ENEMIES HUD ###

def enemy_display():

    e_display = '\nENEMY STATS\nHP: {} ATK: {} DEF: {}\n'.format(slime.e_health,slime.e_attack,slime.e_defense)
    print(e_display)

### CHARACTER SELECTION ###

def char_select():
    global title
    for x in char_list:
        print(x)

    adventurer = input('Please choose a class: ')

    #### Determins name for class you chose ###
    if adventurer.upper() not in char_list:
        while adventurer.upper() not in char_list:
            for x in char_list:
                print(x.upper())

            adventurer = input("That's not a class, please choose one:")

            player.title = adventurer.upper()
    else:
        player.title = adventurer.upper()

### EXPERIENCE GAIN ###
def exp():
   exp_gain = (float(slime.e_health) * 0.5)
    
    if exp_gain =

### ACTUAL CODE ###

intro_text()
char_select()

intro_battle()

if player.health <= 0:
    print("\n\nIt seems you weren't the hero we were looking for...")

else:
    print("\n\nExcellent job! You are the hero!")

