import random

class Adventurer:

    def __init__(job, name, lvl, hp, atk, arm, spd, mag, res):

        job.name = name
        job.lvl = lvl
        job.hp = hp
        job.atk = atk
        job.arm = arm
        job.spd = spd
        job.mag = mag
        job.res = res


#scope = how much the code sees at once
#Assigns the class for a specific person

#Gives Adventurer an Identity [need to find a way to randomize stats
Thief = Adventurer('Thief', 1, random.randint(6,10), random.randint(3,7), random.randint(2,5), random.randint(5,8), random.randint(1,4),
                   random.randint(3,5))

print('{}: Lvl {}'.format(Thief.name, Thief.lvl))

print('\tHP: {} \n\tATK: {} \n\tARM: {} \n\tSPD: {} \n\tMAG: {} \n\tRES: {}'.format(Thief.hp, Thief.atk, Thief.arm, Thief.spd, Thief.mag, Thief.res))
#Prints stats for the Adventurer