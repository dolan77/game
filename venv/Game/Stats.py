import random

attack = random.randint(1,10)

defense = random.randint(1,10)

speed = random.randint(1,10)

health = random.randint(4,10)

Level = 1
#class names: Thief, Hero, Tank, Berserker, Clown

#Assigning a class
if speed >= 6:
    name = 'Thief'
    attack = random.randint(1,4)
    defense = random.randint(1,3)

elif 4 <= attack <= 5 and 4 <= defense <= 5 and 4 <= speed <= 5:
    name = "Hero"

#CAN MAKE A SUB CLASS
elif attack >= 7 and health <= 8:
    if defense >= 4:
        name = "DEFENSE Berserker"
    else:
        name = "ATTACK Berserker"

elif defense >= 6 and health >= 6:
    name = "Tank"
    speed = random.randint(1,3)
else:
    name = 'Clown'