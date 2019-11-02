import random

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





enemystat = [2,3]
basestats = [4,4,4,3,3]
list = ['THIEF', 'HERO', 'TANK', 'BERSERKER']

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


### PLAYER AND ENEMIES ###
player = Adventurer(title,random.choice(basestats),random.choice(basestats),random.choice(basestats),random.choice(basestats))

enemy1 = enemy(random.randint(4,5),random.choice(enemystat),random.choice(enemystat),random.choice(enemystat))

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
        print('\nThe enemy takes no damage')
        dealt = 0
    else:
        print('\nYou deal {} damage'.format(dealt))
        enemy1.e_health = enemy1.e_health - dealt

### FUNCTION FOR THE DAMAGE THE PLAYER RECEIVES ###
def damage_receive():
    receive = enemy1.e_attack - player.defense

    if receive <= 0:
        print('\nYou take no damage')
        receive = 0

    else:
        print('You take {} damage\n'.format(receive))
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

        else:
            pass

        damage_receive()