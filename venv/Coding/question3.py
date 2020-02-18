# import math
# I_high = 0
# I_low = 0
# C_high = -1
# C_low = -2
# C_p = 0
# count = 1
# Ip = ((I_high - I_low) / (C_high - C_low)) * (C_p - C_low) + I_low
# PM_10 = -1
# PM_25 = -1
# NO_2 = -1
# max = 0
# quality = 0
#
# def PM_25_calc(C_p):
#
#     ## GOOD QUALITY ###
#     if 0 <= PM_25 <= 12.0:
#         global quality
#         quality = "Good"
#         # PM_25_constant(C_p)
#         # Ip = ((I_high - I_low) / (C_high - C_low)) * (C_p - C_low) + I_low
#
#         return (PM_25_constant(C_p))
#
# def PM_25_constant(C_p):
#
#     ## GOOD QUALITY ###
#     if 0 <= PM_25 <= 12.0:
#         C_low = 0
#         C_high = 12.0
#         I_low = 0
#         I_high = 50
#         Ip = ((I_high - I_low) / (C_high - C_low)) * (C_p - C_low) + I_low
#         return (round(Ip))
#
#
#
# user_input = int(input('Air Quality Index Calculator\nHow many locations for this report? '))
#
# for i in range(1, user_input + 1):
#
#         name = input('What is the name of Location {}? '.format(i))
#
#         PM_25 = float(input('\tEnter PM-2.5 concentration: '))
#         print(f'\tPM-2.5 concentration of {PM_25} is index level {PM_25_calc(PM_25)}')
#         PM_25_max = PM_25_calc(PM_25)
#
#         ### FINDS MAXIMUM QUALITY OF AIR ###
#
#         print(f"Air Quality: {quality}\n")

import math

def truncate(f):
    return math.floor(f * 10 ** 1) / 10 ** 1

f = float(input())

print(f'the value of {truncate(f)}')