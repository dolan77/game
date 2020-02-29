import math

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

def PM_25_constant(C_p):

    ## GOOD QUALITY ###
    if 0 <= PM_25 <= 12.0:
        C_low = 0
        C_high = 12.0
        I_low = 0
        I_high = 50
        Ip = ((I_high - I_low) / (C_high - C_low)) * (C_p - C_low) + I_low
        return (round(Ip))

    ## MODERATE QUALITY ###
    elif 12.1 <= PM_25 <= 35.4:
        C_low = 12.1
        C_high = 35.4
        I_low = 51
        I_high = 100
        Ip = ((I_high - I_low) / (C_high - C_low)) * (C_p - C_low) + I_low
        return (round(Ip))

    ## UNHEALTHY FOR SENSITIVE GROUPS QUALITY ##
    elif 35.5 <= PM_25 <= 55.4:
        C_low = 35.5
        C_high = 55.4
        I_low = 101
        I_high = 150
        Ip = ((I_high - I_low) / (C_high - C_low)) * (C_p - C_low) + I_low
        return (round(Ip))

    ## UNHEALTHY QUALITY ##
    elif 55.5 <= PM_25 <= 150.4:
        C_low = 55.5
        C_high = 150.4
        I_low = 151
        I_high = 200
        Ip = ((I_high - I_low) / (C_high - C_low)) * (C_p - C_low) + I_low
        return (round(Ip))

    ## VERY UNHEALTHY QUALITY ##
    elif 150.5 <= PM_25 <= 250.4:
        C_low = 150.5
        C_high = 250.4
        I_low = 201
        I_high = 300
        Ip = ((I_high - I_low) / (C_high - C_low)) * (C_p - C_low) + I_low
        return (round(Ip))

    ## HAZARDOUS QUALITY ##
    elif 250.5 <= PM_25 <= 500.4:
        C_low = 250.5
        C_high = 500.4
        I_low = 301
        I_high = 500
        Ip = ((I_high - I_low) / (C_high - C_low)) * (C_p - C_low) + I_low
        return (round(Ip))

def NO_2_constant(C_p):
        ## HAZARDOUS QUALITY ##
    if 1250 <= NO_2 <= 2049:
        C_low = 1250
        C_high = 2049
        I_low = 301
        I_high = 500
        Ip = ((I_high - I_low) / (C_high - C_low)) * (C_p - C_low) + I_low
        return round(Ip)

        ## VERY UNHEALTHY QUALITY ##
    elif 650 <= NO_2 <= 1249:
        C_low = 650
        C_high = 1249
        I_low = 201
        I_high = 300
        Ip = ((I_high - I_low) / (C_high - C_low)) * (C_p - C_low) + I_low
        return round(Ip)

        ## UNHEALTHY QUALITY ##
    elif 361 <= NO_2 <= 649:
        C_low = 361
        C_high = 649
        I_low = 151
        I_high = 200
        Ip = ((I_high - I_low) / (C_high - C_low)) * (C_p - C_low) + I_low
        return round(Ip)

        ## UNHEALTHY FOR SENSITIVE GROUPS QUALITY ##
    elif 101 <= NO_2 <= 360:
        C_low = 101
        C_high = 360
        I_low = 101
        I_high = 150
        Ip = ((I_high - I_low) / (C_high - C_low)) * (C_p - C_low) + I_low
        return round(Ip)

        ## MODERATE QUALITY ##
    elif 54 <= NO_2 <= 100:
        C_low = 54
        C_high = 100
        I_low = 51
        I_high = 100
        Ip = ((I_high - I_low) / (C_high - C_low)) * (C_p - C_low) + I_low
        return round(Ip)

        ## GOOD QUALITY ##
    elif 0 <= NO_2 <= 53:
        C_low = 0
        C_high = 53.0
        I_low = 0
        I_high = 50
        Ip = ((I_high - I_low) / (C_high - C_low)) * (C_p - C_low) + I_low
        return round(Ip)

def PM_10_constant(C_p):

        ## HAZARDOUS QUALITY ##
        if 425 <= PM_10 <= 604:
            C_low = 425
            C_high = 604
            I_low = 301
            I_high = 500
            Ip = ((I_high - I_low) / (C_high - C_low)) * (C_p - C_low) + I_low
            return round(Ip)

            ## VERY UNHEALTHY QUALITY ##
        elif 355 <= PM_10 <= 424:
            C_low = 355
            C_high = 424
            I_low = 201
            I_high = 300
            Ip = ((I_high - I_low) / (C_high - C_low)) * (C_p - C_low) + I_low
            return round(Ip)

            ## UNHEALTHY QUALITY ##
        elif 255 <= PM_10 <= 354:
            C_low = 255
            C_high = 354
            I_low = 201
            I_high = 300
            Ip = ((I_high - I_low) / (C_high - C_low)) * (C_p - C_low) + I_low
            return round(Ip)

            ## UNHEALTHY FOR SENSITIVE GROUPS QUALITY##
        elif 155 <= PM_10 <= 254:
            C_low = 155
            C_high = 254
            I_low = 101
            I_high = 150
            Ip = ((I_high - I_low) / (C_high - C_low)) * (C_p - C_low) + I_low
            return round(Ip)

            ## MODERATE QUALITY ##
        elif 55 <= PM_10 <= 154:
            C_low = 55
            C_high = 154
            I_low = 51
            I_high = 100
            Ip = ((I_high - I_low) / (C_high - C_low)) * (C_p - C_low) + I_low
            return round(Ip)

            ## GOOD QUALITY ##
        elif 0 <= PM_10 <= 54:
            C_low = 0
            C_high = 54
            I_low = 0
            I_high = 50
            Ip = ((I_high - I_low) / (C_high - C_low)) * (C_p - C_low) + I_low
            return round(Ip)


def PM_25_calc(C_p):
    global quality

        ## GOOD QUALITY ###
    if 0 <= PM_25 <= 12.0:
        quality = 'Good'
        return (PM_25_constant(C_p))

    ## MODERATE QUALITY ###
    elif 12.1 <= PM_25 <= 35.4:
        quality = 'Moderate'
        return (PM_25_constant(C_p))

    ## UNHEALTHY FOR SENSITIVE GROUPS QUALITY ##
    elif 35.5 <= PM_25 <= 55.4:
        quality = 'Unhealthy For Sensitive Groups'
        return (PM_25_constant(C_p))

        ## UNHEALTHY QUALITY ##
    elif 55.5 <= PM_25 <= 150.4:
        quality = 'Unhealthy'
        return (PM_25_constant(C_p))

        ## VERY UNHEALTHY QUALITY ##
    elif 150.5 <= PM_25 <= 250.4:
        quality = 'Very Unhealthy'
        return (PM_25_constant(C_p))

        ## HAZARDOUS QUALITY ##
    elif 250.5 <= PM_25 <= 500.4:
        quality = 'Hazardous'
        return (PM_25_constant(C_p))


def PM_10_calc(C_p):
    global quality
        ## HAZARDOUS QUALITY ##
    if 425 <= PM_10 <= 604:
        quality = 'Hazardous'
        return (PM_10_constant(C_p))

        ## VERY UNHEALTHY QUALITY ##
    elif 355 <= PM_10 <= 424:
        quality = 'Very Unhealthy'
        return (PM_10_constant(C_p))

        ## UNHEALTHY QUALITY ##
    elif 255 <= PM_10 <= 354:
        quality = 'Unhealthy'
        return (PM_10_constant(C_p))

        ## UNHEALTHY FOR SENSITIVE GROUPS QUALITY##
    elif 155 <= PM_10 <= 254:
        quality = 'Unhealthy For Sensitive Groups'
        return (PM_10_calc(C_p))

        ## MODERATE QUALITY ##
    elif 55 <= PM_10 <= 154:
        quality = 'Moderate'
        return (PM_10_constant(C_p))

        ## GOOD QUALITY ##
    elif 0 <= PM_10 <= 54:
        quality = 'Good'
        return (PM_10_constant(C_p))

def NO_2_calc(C_p):

    global quality

        ## HAZARDOUS QUALITY ##
    if 1250 <= NO_2 <= 2049:
        quality = 'Hazardous'
        return (NO_2_constant(C_p))

        ## VERY UNHEALTHY QUALITY ##
    elif 650 <= NO_2 <= 1249:
        quality = 'Very Unhealthy'
        return (NO_2_constant(C_p))

            ## UNHEALTHY QUALITY ##
    elif 361 <= NO_2 <= 649:
        quality = 'Unhealthy'
        return (NO_2_constant(C_p))

        ## UNHEALTHY FOR SENSITIVE GROUPS QUALITY ##
    elif 101 <= NO_2 <= 360:
        quality = 'Unhealthy For Sensitive Groups'
        return (NO_2_constant(C_p))

        ## MODERATE QUALITY ##
    elif 54 <= NO_2 <= 100:
        quality = 'Moderate'
        return (NO_2_constant(C_p))

        ## GOOD QUALITY ##
    elif 0 <= NO_2 <= 53:
        quality = 'Good'
        return (NO_2_constant(C_p))


        ### FORMULA TO FIND THE MAXIMUM VALUE OF THE AQI ###
def Max(a , b , c):

    Max = a
    PM_25_calc(PM_25)

    if b > Max:
        Max = b
        PM_10_calc(PM_10)

    if c > Max:
        Max = c
        NO_2_calc(NO_2)

    return Max

### TRUNCATE ###
def truncate(f):
    return math.floor(f * 10 ** 1) / 10 ** 1


user_input = int(input('Air Quality Index Calculator' + '\nHow many locations for this report? '))

for i in range (1 , user_input + 1):

    name = input(f'What is the name of Location {i}?')

    PM_25 = float(input(' -> Enter PM-2.5 concentration: '))
    print(f'\tPM-2.5 concentration of {truncate(PM_25)}' + f'is index level {PM_25_calc(PM_25)}')
    PM_25_max = PM_25_calc(PM_25)

    PM_10 = math.floor(float(input(' -> Enter PM-10 concentration: ')))
    print(f'\tPM-10 concentration of {PM_10} is index level {PM_10_calc(PM_10)}')
    PM_10_max = PM_10_calc(PM_10)

    NO_2 = math.floor(float(input(' -> Enter NO-2 concentration: ')))
    print(f'\tNO-2 concentration of {NO_2} is index level {NO_2_calc(NO_2)}')
    NO_2_max = NO_2_calc(NO_2)

    print(f'\nAQI for {name} is {Max(PM_25_max , PM_10_max, NO_2_max)}')
    print(f"Air Quality: {quality}\n")
