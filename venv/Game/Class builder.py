from Stats import attack, defense, speed, Level, health, name

#likelyhood of being a good adventurer
total_stats = attack + defense + speed + health

#Gives display of stats
def display ():
   return 'Class: {}\nLevel: {}\nHealth: {}\nAttack: {}\nDefense: {}\nSpeed: {}'.format(name, Level, health, attack, defense, speed)

if total_stats <= 15:
    print("You're not fit to be an Adventurer.")

if total_stats >15:
    print("You can be an Adventurer.")

print(display())