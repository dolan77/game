 ### CODE TESTING ###

import random

xp = 100
level = 1
nextlvl = 25
hp = 5
attack = 3

while xp >= nextlvl:
    level += 1
    hp += 5
    attack += 2
    nextlvl = round(nextlvl * 1.5)


print(level)
print(nextlvl)
print(hp)
print(attack)