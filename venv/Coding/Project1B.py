import math

## INITIALIZING THE VARIABLES TO SOVLE FOR AQI ###
I_high = 0
I_low = 0
C_high = -1
C_low = -2
C_p = 0
count = 1
Ip = ((I_high - I_low) / (C_high - C_low)) * (C_p - C_low) + I_low

## INITIALIZE VARIABLES FOR THE CONCENTRATIONS ##
PM_10 = -1
PM_25 = -1
NO_2 = -1
SO = -1
CO = -1
O_2 = -1

max = 0
quality = 0

### FUNCTIONS FOR THE CONCENTRATION CONSTANTS ###
def PM_25_constant(C_p):

    if PM_25 < 0:
        pass

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

def SO_constant(C_p):

    ## GOOD QUALITY ##
    if 0 <= SO <= 35:
        C_low = 0
        C_high = 35.0
        I_low = 0
        I_high = 50
        Ip = ((I_high - I_low) / (C_high - C_low)) * (C_p - C_low) + I_low
        return round(Ip)

    ## MODERATE QUALITY ##
    elif 36 <= SO <= 75:
        C_low = 36
        C_high = 75.0
        I_low = 51
        I_high = 100
        Ip = ((I_high - I_low) / (C_high - C_low)) * (C_p - C_low) + I_low
        return round(Ip)

    ## UNHEALTHY FOR SENSITIVE GROUPS QUALITY ##
    elif 76 <= SO <= 185:
        C_low = 76
        C_high = 185.0
        I_low = 101
        I_high = 150
        Ip = ((I_high - I_low) / (C_high - C_low)) * (C_p - C_low) + I_low
        return round(Ip)

    ## UNHEALTHY QUALITY ##
    elif 186 <= SO <= 304:
        C_low = 186
        C_high = 304.0
        I_low = 151
        I_high = 200
        Ip = ((I_high - I_low) / (C_high - C_low)) * (C_p - C_low) + I_low
        return round(Ip)

    ## VERY UNHEALTHY QUALITY ##
    elif 305 <= SO <= 604:
        C_low = 305
        C_high = 604.0
        I_low = 201
        I_high = 300
        Ip = ((I_high - I_low) / (C_high - C_low)) * (C_p - C_low) + I_low
        return round(Ip)

    ## HAZARDOUS ##
    elif 605 <= SO <= 1004:
        C_low = 605
        C_high = 1004.0
        I_low = 301
        I_high = 500
        Ip = ((I_high - I_low) / (C_high - C_low)) * (C_p - C_low) + I_low
        return round(Ip)

def CO_constant(C_p):

    ## GOOD QUALITY ##
    if 0 <= CO <= 4.4:
        C_low = 0
        C_high = 4.4
        I_low = 0
        I_high = 50
        Ip = ((I_high - I_low) / (C_high - C_low)) * (C_p - C_low) + I_low
        return round(Ip)

    ## MODERATE QUALITY ##
    elif 4.5 <= CO <= 9.4:
        C_low = 4.5
        C_high = 9.4
        I_low = 51
        I_high = 100
        Ip = ((I_high - I_low) / (C_high - C_low)) * (C_p - C_low) + I_low
        return round(Ip)

    ## UNHEALTHY FOR SENSITIVE GROUPS QUALITY ##
    elif 9.5 <= CO <= 12.4:
        C_low = 9.5
        C_high = 12.4
        I_low = 101
        I_high = 150
        Ip = ((I_high - I_low) / (C_high - C_low)) * (C_p - C_low) + I_low
        return round(Ip)

    ## UNHEALTHY QUALITY ##
    elif 12.5 <= CO <= 15.4:
        C_low = 12.5
        C_high = 15.4
        I_low = 151
        I_high = 200
        Ip = ((I_high - I_low) / (C_high - C_low)) * (C_p - C_low) + I_low
        return round(Ip)

    ## VERY UNHEALTHY QUALITY ##
    elif 15.5 <= CO <= 30.4:
        C_low = 15.5
        C_high = 30.4
        I_low = 201
        I_high = 300
        Ip = ((I_high - I_low) / (C_high - C_low)) * (C_p - C_low) + I_low
        return round(Ip)

    ## HAZARDOUS QUALITY ##
    elif 30.5 <= CO <= 50.4:
        C_low = 30.5
        C_high = 50.4
        I_low = 301
        I_high = 500
        Ip = ((I_high - I_low) / (C_high - C_low)) * (C_p - C_low) + I_low
        return round(Ip)

def O_3_constant(C_p):

    ## GOOD AND MODERATE QUALITY ##
    if 0 <= O_3 <= 124:
        pass

    #UNHEALTHY FOR SENSITIVE GROUPS QUALITY ##
    elif 125 <= O_3 <= 164:
        C_low = 125
        C_high = 164
        I_low = 101
        I_high = 150
        Ip = ((I_high - I_low) / (C_high - C_low)) * (C_p - C_low) + I_low
        return round(Ip)

    ## UNHEALTHY QUALITY ##
    elif 165 <= O_3 <= 204:
        C_low = 165
        C_high = 204
        I_low = 151
        I_high = 200
        Ip = ((I_high - I_low) / (C_high - C_low)) * (C_p - C_low) + I_low
        return round(Ip)

    # VERY UNHEALTHY QUALITY ##
    elif 205 <= O_3 <= 404:
        C_low = 205
        C_high = 404
        I_low = 201
        I_high = 300
        Ip = ((I_high - I_low) / (C_high - C_low)) * (C_p - C_low) + I_low
        return round(Ip)

    ## HAZARDOUS QUALITY ##
    elif 405 <= O_3 <= 604:
        C_low = 405
        C_high = 604
        I_low = 301
        I_high = 500
        Ip = ((I_high - I_low) / (C_high - C_low)) * (C_p - C_low) + I_low
        return round(Ip)



def PM_25_calc(C_p):
    global quality

    if PM_25 < 0:
        pass
        return(-1)

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

    if PM_10 < 0:
        return(-1)

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

    if NO_2 < 0:
        return(-1)

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


def SO_calc(C_p):

    global quality

    if SO < 0:
        return(-1)

        ## HAZARDOUS QUALITY ##
    if 605 <= SO <= 1004:
        quality = 'Hazardous'
        return (SO_constant(C_p))

        ## VERY UNHEALTHY QUALITY ##
    elif 305 <= SO <= 604:
        quality = 'Very Unhealthy'
        return (SO_constant(C_p))

            ## UNHEALTHY QUALITY ##
    elif 186 <= SO <= 304:
        quality = 'Unhealthy'
        return (SO_constant(C_p))

        ## UNHEALTHY FOR SENSITIVE GROUPS QUALITY ##
    elif 76 <= SO <= 185:
        quality = 'Unhealthy For Sensitive Groups'
        return (SO_constant(C_p))

        ## MODERATE QUALITY ##
    elif 36 <= SO <= 75:
        quality = 'Moderate'
        return (SO_constant(C_p))

        ## GOOD QUALITY ##
    elif 0 <= SO <= 35:
        quality = 'Good'
        return (SO_constant(C_p))

def CO_calc(C_p):

    global quality

    if CO < 0:
        return (-1)

        ## HAZARDOUS QUALITY ##
    if 30.5 <= CO <= 50.4:
        quality = 'Hazardous'
        return (CO_constant(C_p))

        ## VERY UNHEALTHY QUALITY ##
    elif 15.5 <= CO <= 30.4:
        quality = 'Very Unhealthy'
        return (CO_constant(C_p))

            ## UNHEALTHY QUALITY ##
    elif 12.5 <= CO <= 15.4:
        quality = 'Unhealthy'
        return (CO_constant(C_p))

        ## UNHEALTHY FOR SENSITIVE GROUPS QUALITY ##
    elif 9.5 <= CO <= 12.4:
        quality = 'Unhealthy For Sensitive Groups'
        return (CO_constant(C_p))

        ## MODERATE QUALITY ##
    elif 4.5 <= CO <= 9.4:
        quality = 'Moderate'
        return (CO_constant(C_p))

        ## GOOD QUALITY ##
    elif 0 <= CO <= 4.4:
        quality = 'Good'
        return (CO_constant(C_p))

def O_3_calc(C_p):

    global quality

    if O_3 < 0:
        return(-1)

    ## HAZARDOUS QUALITY ##
    if 405 <= O_3 <= 604:
        quality = 'Hazardous'
        return (O_3_constant(C_p))

        ## VERY UNHEALTHY QUALITY ##
    elif 205 <= O_3 <= 404:
        quality = 'Very Unhealthy'
        return (O_3_constant(C_p))

        ## UNHEALTHY QUALITY ##
    elif 165 <= O_3 <= 204:
        quality = 'Unhealthy'
        return (O_3_constant(C_p))

        ## UNHEALTHY FOR SENSITIVE GROUPS QUALITY ##
    elif 125 <= O_3 <= 164:
        quality = 'Unhealthy For Sensitive Groups'
        return (O_3_constant(C_p))

    elif O_3 < 125:
        return(-1)

### FORMULA TO FIND THE MAXIMUM VALUE OF THE AQI ###

def Max(a , b , c , d , e , f):

    Max = a
    PM_25_calc(PM_25)

    if b > Max:
        Max = b
        PM_10_calc(PM_10)

    elif c > Max:
        Max = c
        NO_2_calc(NO_2)

    elif d > Max:
        Max = d
        SO_calc(SO)

    elif e > Max:
        Max = e
        CO_calc(CO)

    elif f > Max:
        Max = f
        O_3_calc(O_3)

    return Max

### TRUNCATE ###
def truncate(f):
    return math.floor(f * 10 ** 1) / 10 ** 1



user_input = int(input('Air Quality Index Calculator' + '\nHow many locations for this report? ')) # INPUT 1 #

while user_input <= 0:
    user_input = int(input('How many locations for this report? ')) # INPUT 2 #


for i in range (1 , user_input + 1):

    max = 0

    name = input(f'What is the name of Location {i}? ') # INPUT 3 #

    PM_25 = float(input(' -> Enter PM-2.5 concentration: ')) # INPUT 4 #
    if PM_25_calc(PM_25) < 0:
        pass

    else:
        print(f'\tPM-2.5 concentration of {truncate(PM_25)}' + f'is index level {PM_25_calc(PM_25)}') # PRINT 1 #
        PM_25_max = PM_25_calc(PM_25)


    PM_10 = math.floor(float(input(' -> Enter PM-10 concentration: '))) # INPUT 5 #
    if PM_10_calc(PM_10) < 0:
        pass
    else:
        print(f'\tPM-10 concentration of {PM_10} is index level {PM_10_calc(PM_10)}') # PRINT 2 #
        PM_10_max = PM_10_calc(PM_10)


    NO_2 = math.floor(float(input(' -> Enter NO-2 concentration: '))) # INPUT 6 #
    if NO_2_calc(NO_2) < 0:
        pass
    else:
        print(f'\tNO-2 concentration of {NO_2} is index level {NO_2_calc(NO_2)}') # PRINT 3 #
        NO_2_max = NO_2_calc(NO_2)


    SO = math.floor(float(input(' -> Enter SO-2 concentration: '))) # INPUT 7 #
    if SO_calc(SO) < 0:
        pass
    else:
        print(f'\tSO-2 concentration of {SO} is index level {SO_calc(SO)}') # PRINT 4 #
        SO_2_max = SO_calc(SO)


    CO = float(input(' -> Enter CO concentration: ')) # INPUT 8 #
    if CO_calc(CO) < 0:
        pass
    else:
        print(f'\tCO concentration of {truncate(CO)} is index level {CO_calc(CO)}') # PRINT 5 #
        CO_max = CO_calc(CO)

    O_3 = math.floor(float(input(' -> Enter O3 concentration: '))) # INPUT 9 #
    if SO_calc(SO) < 125:
        pass
    else:
        print(f'\tO3 concentration of {O_3} is index level {O_3_calc(O_3)}') # PRINT 6 #
        O_3_max = O_3_calc(O_3)

    print(f'\nAQI for {name} is {Max(PM_25_max , PM_10_max, NO_2_max , SO_2_max , CO , O_3)}') # PRINT 7 #
    print(f"Air Quality: {quality}\n") # PRINT 8 #

