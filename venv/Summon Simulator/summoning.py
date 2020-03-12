# Chance of a 5 star: 3%
# Chance of a 4 star: 35%
# Chance of a 3 star: 62%
# Chance of a 2 star:
# Chance of a 1 star:

# list of the units that will go in specific lists depending on their rarirty

ultra_rare_list = []

super_rare_list = []

rare_list = []

# summoning function, lowest percentage will be the rarest while the higher percentage will be least rare

def summon_list(percent):
    if percent <= 0.15:
        unit = 'test'

    elif 0.15 < percent <= 0.35:
        unit = 'rest'

    elif percent > 0.35:
        unit = 'crest'

    return unit


# main function that will run the summon simulator code

def main():

    interface = True

    while interface == True:

        user_input = input('Would you like to roll for a unit? [yes / no] ')

        while user_input.lower() not in ['yes' , 'no']:

            user_input = input('Please enter a valid input: [yes / no] ')

        if user_input.lower() == 'yes':

            percentage = round(random.random() , 2)

            print(summon_list(percentage))

        else:
            print('no got chosen')
            interface = False

