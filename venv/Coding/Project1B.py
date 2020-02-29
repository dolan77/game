import math

### DECLARING VARIABLES AND MAKING THE LIST TO STORE NAMES FOR LOCATION AND THEIR MAX AQI ###
max = 0
quality = 0

name_list = []
max_value = []
PM25_counter = 0

### THE FORMULA TO SOLVE FOR THE AQI ###
def formula(C_high, C_low, I_low, I_high, C_pollutant):
    Ip = ((I_high - I_low) / (C_high - C_low)) * (C_pollutant- C_low) + I_low
    return (round(Ip))

### DETERMINES QUALITY BASED ON THE GIVEN AQI ###
def QUALITY (AQI):

    if 0 <= AQI <= 50:
        quality = 'Good'

    elif 51 <= AQI <= 100:
        quality = 'Moderate'

    elif 101 <= AQI <= 150:
        quality = 'Unhealthy for Sensitive Groups'

    elif 151 <= AQI <= 200:
        quality = 'Unhealthy'

    elif 201 <= AQI <= 300:
        quality = 'Very Unhealthy'

    elif 301 <= AQI <= 500:
        quality = 'Hazardous'

    return quality


### FUNCTION TO SOLVE THE USER'S INPUT OF PM_2.5 CONCENTRATION, WILL COMPARE VALUE OF PM2.5 AND RETURN AQI ###
def PM_25_calc(C_pollutant):

    if PM_25 < 0:
        value = (-1)

    ## GOOD QUALITY ###
    if PM_25 <= 12.0:
        value = (formula(12, 0, 0, 50, C_pollutant))

    ## MODERATE QUALITY ###
    elif PM_25 <= 35.4:
        value = (formula(35.4, 12.1, 51, 100, C_pollutant))

    ## UNHEALTHY FOR SENSITIVE GROUPS QUALITY ##
    elif PM_25 <= 55.4:
        value = (formula(55.4, 35.5, 101, 150, C_pollutant))

    ## UNHEALTHY QUALITY ##
    elif PM_25 <= 150.4:
        value = (formula(150.4, 55.5, 151, 200, C_pollutant))

    ## VERY UNHEALTHY QUALITY ##
    elif PM_25 <= 250.4:
        value = (formula(250.4, 150.5, 201, 300, C_pollutant))

    ## HAZARDOUS QUALITY ##
    elif PM_25 <= 500.4:
        value = (formula(500.4, 250.5, 301, 500, C_pollutant))

    return value


### FUNCTION TO SOLVE THE USER'S INPUT OF PM_10 CONCENTRATION, WILL COMPARE VALUE OF PM10 AND RETURN AQI ###
def PM_10_calc(C_pollutant):

    ## HAZARDOUS QUALITY ##
    if 425 <= PM_10 <= 604:

        value = (formula(604, 425, 301, 500, C_pollutant))

        ## VERY UNHEALTHY QUALITY ##
    elif 355 <= PM_10 <= 424:

        value = formula(424, 355, 201, 300, C_pollutant)

        ## UNHEALTHY QUALITY ##
    elif 255 <= PM_10 <= 354:

        value = formula(354, 255, 201, 300, C_pollutant)

        ## UNHEALTHY FOR SENSITIVE GROUPS QUALITY##
    elif 155 <= PM_10 <= 254:

        value = formula(254, 155, 101, 150, C_pollutant)

        ## MODERATE QUALITY ##
    elif 55 <= PM_10 <= 154:

        value = formula(154, 55, 51, 100, C_pollutant)

        ## GOOD QUALITY ##
    elif 0 <= PM_10 <= 54:

        value = formula(54, 0, 0, 50, C_pollutant)

    elif PM_10 < 0:
        value =(-1)

    return value


### FUNCTION TO SOLVE THE USER'S INPUT OF NO_2 CONCENTRATION, WILL COMPARE VALUE OF NO_2 AND RETURN AQI ###
def NO_2_calc(C_pollutant):

    ## HAZARDOUS QUALITY ##
    if 1250 <= NO_2 <= 2049:

        value = formula(2049, 1250, 301, 500, C_pollutant)

        ## VERY UNHEALTHY QUALITY ##
    elif 650 <= NO_2 <= 1249:

        value = formula(1249, 650, 201, 300, C_pollutant)

        ## UNHEALTHY QUALITY ##
    elif 361 <= NO_2 <= 649:

        value = formula(649, 361, 151, 200, C_pollutant)

        ## UNHEALTHY FOR SENSITIVE GROUPS QUALITY ##
    elif 101 <= NO_2 <= 360:

        value = formula(360, 101, 101, 150, C_pollutant)

        ## MODERATE QUALITY ##
    elif 54 <= NO_2 <= 100:

        value = formula(100, 54, 51, 100, C_pollutant)

        ## GOOD QUALITY ##
    elif 0 <= NO_2 <= 53:

        value = formula (53, 0, 0, 50, C_pollutant)

    elif NO_2 < 0:
        value = -1

    return value


### FUNCTION TO SOLVE THE USER'S INPUT OF SO CONCENTRATION, WILL COMPARE VALUE OF SO AND RETURN AQI ###
def SO_calc(C_pollutant):


    if SO < 0:
        value = -1

    ## GOOD QUALITY ##
    elif 0 <= SO <= 35:

        value = formula(35, 0, 0, 50, C_pollutant)

    ## MODERATE QUALITY ##
    elif 36 <= SO <= 75:

        value = formula(75, 36, 51, 100, C_pollutant)

    ## UNHEALTHY FOR SENSITIVE GROUPS QUALITY ##
    elif 76 <= SO <= 185:

        value = formula(185, 76, 101, 150, C_pollutant)

    ## UNHEALTHY QUALITY ##
    elif 186 <= SO <= 304:

        value = formula(304, 186, 151, 200, C_pollutant)

    ## VERY UNHEALTHY QUALITY ##
    elif 305 <= SO <= 604:

        value = formula(604, 305, 201, 300, C_pollutant)

    ## HAZARDOUS ##
    elif 605 <= SO <= 1004:

        value = formula(1004, 605, 301, 500, C_pollutant)

    return value


### FUNCTION TO SOLVE THE USER'S INPUT OF CO CONCENTRATION, WILL COMPARE VALUE OF CO AND RETURN AQI ###
def CO_calc(C_pollutant):

    ## GOOD QUALITY ##
    if 0 <= CO <= 4.4:

        value = formula(4.4, 0, 0, 50, C_pollutant)

    ## MODERATE QUALITY ##
    elif 4.5 <= CO <= 9.4:

        value = formula(9.4, 4.5, 51, 100, C_pollutant)

    ## UNHEALTHY FOR SENSITIVE GROUPS QUALITY ##
    elif 9.5 <= CO <= 12.4:

        value = formula(12.4, 9.5, 101, 150, C_pollutant)

    ## UNHEALTHY QUALITY ##
    elif 12.5 <= CO <= 15.4:

        value = formula(15.4, 12.5, 151, 200, C_pollutant)

    ## VERY UNHEALTHY QUALITY ##
    elif 15.5 <= CO <= 30.4:

        value = formula (30.4, 15.5, 201, 300, C_pollutant)

    ## HAZARDOUS QUALITY ##
    elif 30.5 <= CO <= 50.4:

        value = formula (50.4, 30.5, 301, 500, C_pollutant)

    elif CO < 0:
        value = -1

    return value

###   FUNCTION TO SOLVE THE USER'S INPUT OF O_3 CONCENTRAION , WILL COMPARE THE VALUE OF O3 AND RETURN THE AQI ###

def O_3_calc(C_pollutant):

    ## GOOD AND MODERATE QUALITY ##
    if O_3 <= 124:
        value = -1

    #UNHEALTHY FOR SENSITIVE GROUPS QUALITY ##
    elif 125 <= O_3 <= 164:

        value = formula(164, 125, 101, 150, C_pollutant)

    ## UNHEALTHY QUALITY ##
    elif 165 <= O_3 <= 204:

        value = formula (204, 165, 151, 200, C_pollutant)

    # VERY UNHEALTHY QUALITY ##
    elif 205 <= O_3 <= 404:

        value = formula (404, 205, 201, 300, C_pollutant)

    ## HAZARDOUS QUALITY ##
    elif 405 <= O_3 <= 604:

        value = formula (604, 405, 301, 500, C_pollutant)

    return value

### FORMULA TO FIND THE MAXIMUM VALUE OF THE AQI GIVEN THE CONCENTRATION OF ALL 6 VALUES###
def Max (PM_25 , PM_10 , NO_2 , SO , CO , O_3):

    max_list = [PM_25 , PM_10 , NO_2 , SO , CO , O_3]
    Max = 0
    c = 0

    ### GOES THROUGH THE MAX_LIST TO FIND WHICH VALUE IS THE HIGHEST ###
    for i in max_list:

        if i > Max or c == 0:
            Max = i
            c += 1

    return Max


### TRUNCATE FUNCTION TO TRUNCATE THE VALUE OF PM 2.5 AND CO TO THE NEAREST DECIMAL###
def truncate(value):
    return math.floor(value * 10 ** 1) / 10 ** 1


### ASKS USER FOR NUMBER OF LOCATIONS AND PERFORMS AN INPUT VALIDATION IN CASE THEY INPUT AN INSUFFICIENT AMOUNT OF LOCATIONS ###
user_input = int(input('Air Quality Index Calculator' + '\nHow many locations for this report? ')) # INPUT 1 #

while user_input <= 0:
    user_input = int(input('How many locations for this report? ')) # INPUT 2 #


### LOOP THAT SOLVES THE CONCENTRATION VALUES AND OUTPUTS THE MAX AIR QUALITY ###
count = 0

for i in range (1 , user_input + 1):

    name = input(f'What is the name of Location {i}? ') # INPUT 3 #

    ### INPUT FOR CONCENTRATION OF PM2.5 ###
    PM_25 = float(input(' -> Enter PM-2.5 concentration: ')) # INPUT 4 #

    PM_25 = truncate(PM_25)
    ### USED TO HELP SOLVE THE PM2.5 AVERAGE. IF THE USER'S INPUT OF PM 2.5 IS GREATER THAN 0, IT WILL BE ADDED TO THE COUNTER ###
    if PM_25 >= 0:
        PM25_counter += PM_25
        count += 1


    ### CHECKS TO SEE IF THE PM2.5 CONCENTRATION IS LESS THAN 0, WILL GIVE MAX -1 IF SO AND NOT PRINT CONCENTRATION ###
    if PM_25 < 0:
        PM_25_max = PM_25_calc(PM_25)

    else:
        print(f'\tPM-2.5 concentration of {PM_25}' + f' is index level {PM_25_calc(PM_25)}') # PRINT 1 #
        PM_25_max = PM_25_calc(PM_25)


    ### INPUT FOR CONCENTRATION OF PM10, IF PM10 < 0, WILL MAKE MAX -1 AND NOT PRINT CONCENTRATION ###
    PM_10 = math.floor(float(input(' -> Enter PM-10 concentration: '))) # INPUT 5 #

    ### CHECKS TO SEE IF INPUT PM_10 IS LESS THAN 0 ###
    if PM_10 < 0:
        PM_10_max = PM_10_calc(PM_10)
    else:
        print(f'\tPM-10 concentration of {PM_10} is index level {PM_10_calc(PM_10)}') # PRINT 2 #
        PM_10_max = PM_10_calc(PM_10)


    ### INPUT FOR CONCENTRATION OF NO_2, IF NO_2 < 0, WILL MAKE MAX -1 AND NOT PRINT CONCENTRATION ###
    NO_2 = math.floor(float(input(' -> Enter NO-2 concentration: '))) # INPUT 6 #
    if NO_2 < 0:
        NO_2_max = NO_2_calc(NO_2)
    else:
        print(f'\tNO-2 concentration of {NO_2} is index level {NO_2_calc(NO_2)}') # PRINT 3 #
        NO_2_max = NO_2_calc(NO_2)


    ### INPUT FOR CONCENTRATION OF SO, IF SO < 0, WILL MAKE MAX -1 AND NOT PRINT CONCENTRATION ###
    SO = math.floor(float(input(' -> Enter SO-2 concentration: '))) # INPUT 7 #
    if SO < 0:
        SO_2_max = SO_calc(SO)
    else:
        print(f'\tSO-2 concentration of {SO} is index level {SO_calc(SO)}') # PRINT 4 #
        SO_2_max = SO_calc(SO)


    ### INPUT FOR CONCENTRATION OF CO, IF CO < 0, WILL MAKE MAX -1 AND NOT PRINT THE CONCENTRATION ###
    CO = float(input(' -> Enter CO concentration: ')) # INPUT 8 #
    CO = truncate(CO)
    if CO < 0:
        CO_max = CO_calc(CO)
    else:
        print(f'\tCO concentration of {CO} is index level {CO_calc(CO)}') # PRINT 5 #
        CO_max = CO_calc(CO)


    ### INPUT FOR CONCENTRATION OF O_3, IF INPUT IS < 125, WILL MAKE MAX -1 AND NOT PRINT THE CONCENTRATION###
    O_3 = math.floor(float(input(' -> Enter O3 concentration: '))) # INPUT 9 #
    if O_3 < 125:
        O_3_max = O_3_calc(O_3)

    else:
        print(f'\tO3 concentration of {O_3} is index level {O_3_calc(O_3)}') # PRINT 6 #
        O_3_max = O_3_calc(O_3)

    AQI = Max(PM_25_max , PM_10_max, NO_2_max , SO_2_max , CO_max , O_3_max)

    ### PRINTS THE AQUI FOR A LOCATION AND GIVES THE AIR QUALITY FOR SAID LOCATION ###
    print(f'\nAQI for {name} is {AQI}') # PRINT 7 #
    print(f"Air Quality: {QUALITY(AQI)}\n") # PRINT 8 #


    ### LIST TO HELP SOLVE FOR THE OVERALL SUMMARY OF THE LOCATIONS, WILL ADD NAME OF LOCATION AND AQI TO APPRORIATE
    # LIST

    name_list.append(name)

    max_value.append(AQI)


### SOLVES FOR THE MAX VALUE GIVEN THE MAXIMUM VALUE OF A LOCATION###
for j in max_value:
    if j > max:
        max = j
        index = max_value.index(j)

## CHECKS TO SEE IF COUNT == 0 AND FORCES IT TO BE -1 SO TO ALLOW A PM25 AVERAGE.
if count == 0:
    count = 1

PM25_avg = PM25_counter / (count)

### USED TO PRINT THE SUMMARY. IF THE PM2.5 AVERAGE IS ABOVE 0, IT WILL PRINT THE AVERAGE CONCENTRATION TOO, OTHERWISE IT DOESN'T ###
if PM25_avg > 0:

    print(f'Summary:\n\tLocation with highest AQI is {name_list[index]} ({max})' + f'\n\tAverage PM-2.5 concentration: {truncate(PM25_avg)}') # PRINT 9 #
else:
    print(f'Summary:\n\tLocation with highest AQI is {name_list[index]} ({max})')  # PRINT 10 #