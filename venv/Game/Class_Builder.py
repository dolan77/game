import random
import sys
import time
import os

### GLOBAL VARIABLES ###

enemy_list = ['SLIME', 'GOBLIN', 'IMP']

enemy_stat = [1,1]

char_list = ['THIEF', 'HERO', 'TANK', 'BERSERKER']

experience = 0

next_level = 25

max_health = 10

e_max_health = 10

### DEFINES ADVENTURER ###

class Adventurer:
    def __init__(stat, title, health, attack, defense, speed, level):
        stat.title = title
        stat.health = health
        stat.attack = attack
        stat.defense = defense
        stat.speed = speed
        stat.level = level

class enemy:
    def __init__(self, name, e_health, e_attack, e_defense, e_speed, level):
        self.name = name
        self.e_health = e_health
        self.e_attack = e_attack
        self.e_defense = e_defense
        self.e_speed = e_speed
        self.level = level


def enemy_health():
    health = player.health + random.randrange(-2, 0)

    return health




### FUNCTION FOR WHEN THE PLAYER DEALS DAMAGE ###
def damage_dealt():
    dealt = player.attack - enemy_1.e_defense

    if dealt <= 0:
        print('\nThe enemy takes 1 damage\n')

        enemy_1.e_health = enemy_1.e_health-1

    else:
        print('\nYou deal {} damage\n'.format(dealt))

        enemy_1.e_health = enemy_1.e_health - dealt




### FUNCTION FOR THE DAMAGE THE PLAYER RECEIVES ###

def damage_receive():
    receive = enemy_1.e_attack - player.defense

    if receive <= 0:
        print('\nYou take 1 damage')
        player.health = player.health -1

    else:
        print('\nYou take {} damage'.format(receive))

        player.health = player.health - receive



### BATTLE SEQUENCE ###

def battle():
    # global e_max_health

    while player.health > 0 and enemy_1.e_health > 0:
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

    if player.health <= 0:
        print('It seems you weren\'t destined to be the savior of this world...')


    ### IF ENEMY IS DEFEATED, CALL'S THIS ###
    else:
        print('You\'ve defeated the enemy!')

        exp_up()

        ### RESETS THE PLAYER AND ENEMIES HEALTH ONCE THE BATTLE IS DONE ###
        player.health = max_health
        # e_max_health = max_health
        # enemy_1.e_health = e_max_health + random.randrange(-2,0)
        enemy_1.e_health = enemy_health()



### PLAYER AND ENEMIES ###
player = Adventurer('Class',max_health,5,4,5,1)

# enemy_1 = enemy(random.choice(enemy_list),random.randint(4,5),random.choice(enemy_stat),random.choice(enemy_stat),random.choice(enemy_stat),(player.level))

enemy_1 = enemy(random.choice(enemy_list),
            enemy_health(),
            player.attack + random.randrange(-2,0),
            player.defense + random.randrange(-2,0),
            player.speed + random.randrange(-2,0),
            10)
            ### CHANGE 10 LATER, THIS IS TO TEST EXP GAINED IN BATTLE ###
            # player.level + random.randrange(0,1))


### ENEMIES HUD ###

def enemy_display():

    e_display = '\n{}\nLVL: {}\nHP: {} ATK: {} DEF: {}'.format(enemy_1.name,enemy_1.level,enemy_1.e_health,enemy_1.e_attack,enemy_1.e_defense)
    print(e_display)




### PLAYER'S HUD ###

def char_display():

    display = ('\nTitle: {}\nHP: {} ATK: {} DEF: {} SPD: {}'.format(player.title,player.health,player.attack,player.defense,player.speed))
    print(display)



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
def exp_up():
    global experience, next_level, max_health

    experience = enemy_1.level * 3

    while experience >= next_level:
        player.level += 1
        experience -= next_level
        next_level = round(next_level * 1.5)

        print('\nYou leveled up! All stats are inceased!')
        player.level += 1
        max_health += 5
        player.attack += 2
        player.defense += 2
        player.speed += 2
        print("\nHere are your new stats! LVL: {} HP: {} ATK: {} DEF: {} SPD: {}".format(player.level,max_health,
                                                                                       player.attack,player.defense,
                                                                                       player.speed))

    else:
        print('\nYou gained {} experience!'.format(experience))
        print('\nLVL: {}\nPROGRESS BAR: {}%\nEXP UNTIL NEXT LVL: {}'.format(player.level, int((experience / next_level) * 100),
                                                                          next_level))





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
    print('Let us test your combat abilities against this enemy!')
    time.sleep(2)
    battle()




### ACTUAL CODE ###

intro_text()
char_select()

intro_battle()

#### TESTING FOR WHEN YOU BATTLE ENEMY AGAIN ###
print('AGAIN')

battle()

# IDEA TO SHOW PROGRESS BAR FOR EXP, NOT PERCENTAGE
# [IIIII   ]




