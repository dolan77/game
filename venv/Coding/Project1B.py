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
user_input = -1

name_list = []
max_value = []
PM25_counter = 0

        ### THE FORMULA TO SOLVE FOR THE AQI ###
def formula(C_high, C_low, I_low, I_high, C_p):
    Ip = ((I_high - I_low) / (C_high - C_low)) * (C_p - C_low) + I_low
    return (round(Ip))


### FUNCTION TO SOLVE THE USER'S INPUT OF PM_2.5 CONCENTRATION ###
def PM_25_calc(C_p):
    global quality

    if PM_25 < 0:
        return (-1)

    ## GOOD QUALITY ###
    if 0 <= PM_25 <= 12.0:
        quality = 'Good'
        return (formula(12, 0, 0, 50, C_p))

    ## MODERATE QUALITY ###
    elif 12.1 <= PM_25 <= 35.4:
        quality = 'Moderate'
        return (formula(35.4, 12.1, 51, 100, C_p))

    ## UNHEALTHY FOR SENSITIVE GROUPS QUALITY ##
    elif 35.5 <= PM_25 <= 55.4:
        quality = 'Unhealthy For Sensitive Groups'
        return (formula(55.4, 35.5, 101, 150, C_p))

    ## UNHEALTHY QUALITY ##
    elif 55.5 <= PM_25 <= 150.4:
        quality = 'Unhealthy'
        return (formula(150.4, 55.5, 151, 200, C_p))

    ## VERY UNHEALTHY QUALITY ##
    elif 150.5 <= PM_25 <= 250.4:
        quality = 'Very Unhealthy'
        return (formula(250.4, 150.5, 201, 300, C_p))

    ## HAZARDOUS QUALITY ##
    elif 250.5 <= PM_25 <= 500.4:
        quality = 'Hazardous'
        return (formula(500.4, 250.5, 301, 500, C_p))


### FUNCTION TO SOLVE THE USER'S INPUT OF PM_10 CONCENTRATION ###
def PM_10_calc(C_p):
    global quality
    ## HAZARDOUS QUALITY ##
    if 425 <= PM_10 <= 604:
        quality = 'Hazardous'
        return (formula(604, 425, 301, 500, C_p))

        ## VERY UNHEALTHY QUALITY ##
    elif 355 <= PM_10 <= 424:
        quality = 'Very Unhealthy'
        return formula(424, 355, 201, 300, C_p)

        ## UNHEALTHY QUALITY ##
    elif 255 <= PM_10 <= 354:
        quality = 'Unhealthy'
        return formula(354, 255, 201, 300, C_p)

        ## UNHEALTHY FOR SENSITIVE GROUPS QUALITY##
    elif 155 <= PM_10 <= 254:
        quality = 'Unhealthy for Senitive Groups'
        return formula(254, 155, 101, 150, C_p)

        ## MODERATE QUALITY ##
    elif 55 <= PM_10 <= 154:
        quality = 'Moderate'
        return formula(154, 55, 51, 100, C_p)

        ## GOOD QUALITY ##
    elif 0 <= PM_10 <= 54:
        quality = 'Good'
        return formula(54, 0, 0, 50, C_p)

    elif PM_10 < 0:
        return(-1)


### FUNCTION TO SOLVE THE USER'S INPUT OF NO_2 CONCENTRATION ###
def NO_2_calc(C_p):
    global quality
    ## HAZARDOUS QUALITY ##
    if 1250 <= NO_2 <= 2049:
        quality = "Hazardous"
        return formula(2049 , 1250 , 301 , 500 , C_p)

        ## VERY UNHEALTHY QUALITY ##
    elif 650 <= NO_2 <= 1249:
        quality = 'Very Unhealthy'
        return formula(1249 , 650 , 201 , 300 , C_p)

        ## UNHEALTHY QUALITY ##
    elif 361 <= NO_2 <= 649:
        quality = 'Unhealthy'
        return formula(649 , 361 , 151 , 200 , C_p)

        ## UNHEALTHY FOR SENSITIVE GROUPS QUALITY ##
    elif 101 <= NO_2 <= 360:
        quality = 'Unhealthy for Sensitive Groups'
        return formula(360 , 101 , 101 , 150 , C_p)

        ## MODERATE QUALITY ##
    elif 54 <= NO_2 <= 100:
        quality = 'Moderate'
        return formula(100 , 54 , 51 , 100 , C_p)

        ## GOOD QUALITY ##
    elif 0 <= NO_2 <= 53:
        quality = 'Good'
        return formula (53 , 0 , 0 , 50 , C_p)

    elif NO_2 < 0:
        return -1


### FUNCTION TO SOLVE THE USER'S INPUT OF SO CONCENTRATION ###
def SO_calc(C_p):

    global quality

    if SO < 0:
        return -1

    ## GOOD QUALITY ##
    elif 0 <= SO <= 35:
        quality = 'Good'
        return formula(35 , 0 , 0 , 50 , C_p)

    ## MODERATE QUALITY ##
    elif 36 <= SO <= 75:
        quality = 'Moderate'
        return formula(75 , 36 , 51 , 100 , C_p)

    ## UNHEALTHY FOR SENSITIVE GROUPS QUALITY ##
    elif 76 <= SO <= 185:
        quality = 'Unhealthy for Sensitive Groups'
        return formula(185 , 76 , 101 , 150 ,C_p)

    ## UNHEALTHY QUALITY ##
    elif 186 <= SO <= 304:
        quality = 'Unhealthy'
        return formula(304 , 186 , 151 , 200 , C_p)

    ## VERY UNHEALTHY QUALITY ##
    elif 305 <= SO <= 604:
        quality = 'Very Unhealthy'
        return formula(604 , 305 , 201 , 300 , C_p)

    ## HAZARDOUS ##
    elif 605 <= SO <= 1004:
        quality = 'Hazardous'
        return formula(1004 , 605 , 301 , 500 , C_p)


### FUNCTION TO SOLVE THE USER'S INPUT OF CO CONCENTRATION ###
def CO_calc(C_p):
    global quality

    ## GOOD QUALITY ##
    if 0 <= CO <= 4.4:
        quality = 'Good'
        return formula(4.4 , 0 , 0 , 50 , C_p)

    ## MODERATE QUALITY ##
    elif 4.5 <= CO <= 9.4:
        quality = 'Moderate'
        return formula(9.4 , 4.5 , 51 , 100 , C_p)

    ## UNHEALTHY FOR SENSITIVE GROUPS QUALITY ##
    elif 9.5 <= CO <= 12.4:
        quality = 'Unhealthy for Sensitive Groups'
        return formula( 12.4 , 9.5 , 101 , 150 , C_p)

    ## UNHEALTHY QUALITY ##
    elif 12.5 <= CO <= 15.4:
        quality = 'Unhealthy'
        return formula( 15.4 , 12.5 , 151 , 200 , C_p)

    ## VERY UNHEALTHY QUALITY ##
    elif 15.5 <= CO <= 30.4:
        quality = 'Very Unhealthy'
        return formula ( 30.4 , 15.5 , 201 , 300 , C_p)

    ## HAZARDOUS QUALITY ##
    elif 30.5 <= CO <= 50.4:
        quality = 'Hazardous'
        return formula ( 50.4 , 30.5 , 301 , 500 , C_p)

    elif CO < 0:
        return -1


### FUNCTION TO SOLVE THE USER'S INPUT OF O_3 CONCENTRAION ###
def O_3_calc(C_p):

    global quality
    ## GOOD AND MODERATE QUALITY ##
    if O_3 <= 124:
        return -1

    #UNHEALTHY FOR SENSITIVE GROUPS QUALITY ##
    elif 125 <= O_3 <= 164:
        quality = 'Unhealthy for Sensitive Groups'
        return formula(164 , 125 , 101 , 150 , C_p)

    ## UNHEALTHY QUALITY ##
    elif 165 <= O_3 <= 204:
        quality = 'Unhealthy'
        return formula (204 , 165 , 151 , 200 , C_p )

    # VERY UNHEALTHY QUALITY ##
    elif 205 <= O_3 <= 404:
        quality = 'Very Unhealthy'
        return formula (404 , 205 , 201 , 300 , C_p)

    ## HAZARDOUS QUALITY ##
    elif 405 <= O_3 <= 604:
        quality = 'Hazardous'
        return formula ( 604 , 405 , 301 , 500 , C_p)


### FORMULA TO FIND THE MAXIMUM VALUE OF THE AQI GIVEN THE CONCENTRATION ###
def Max (PM_25 , PM_10 , NO_2 , SO , CO , O_3):

    max_list = [PM_25 , PM_10 , NO_2 , SO , CO , O_3]
    Max = 0
    c = 0
        ### GOES THROUGH THE MAX_LIST TO FIND WHICH VALUE IS THE HIGHEST ###
    for i in max_list:

        if i > Max or c == 0:
            Max = i
        c += 1

        ### CHECKS TO SEE IF THE MAX VALUES == ONE OF THE ARGUMENTS AND SETS THE QUALITY BASED ON THE CALCULATION ###
    if Max == PM_25:
        PM_25_calc(PM_25)

    elif Max == PM_10:
        PM_10_calc(PM_10)

    elif Max == NO_2:
        NO_2_calc(NO_2)

    elif Max == SO:
        SO_calc(SO)

    elif Max == CO:
        CO_calc(CO)

    elif Max == O_3:
        O_3_calc(O_3)


    return Max


### TRUNCATE FUNCTION TO TRUNCATE THE VALUE OF PM 2.5 AND CO TO THE NEAREST DECIMAL###
def truncate(value):
    return math.floor(value * 10 ** 1) / 10 ** 1



### ASKS USER FOR NUMBER OF LOCATIONS AND PERFORMS AN INPUT VALIDATION IN CASE THEY INPUT AN INSUFFICIENT AMOUNT OF LOCATIONS ###
user_input = int(input('Air Quality Index Calculator' + '\nHow many locations for this report? ')) # INPUT 1 #

while user_input <= 0:
    user_input = int(input('How many locations for this report? ')) # INPUT 2 #



### LOOP THAT SOLVES THE CONCENTRATION VALUES AND OUTPUTS THE MAX AIR QUALITY ###

for i in range (1 , user_input + 1):


    name = input(f'What is the name of Location {i}? ') # INPUT 3 #

    ### INPUT FOR CONCENTRATION OF PM2.5 ###
    PM_25 = float(input(' -> Enter PM-2.5 concentration: ')) # INPUT 4 #

    if PM_25 >= 0:
        PM25_counter += PM_25
        count += 1
        # print(f'Counter: {PM25_counter} Count: {count}')

    else:
        count -= 1
        # print(f'Counter: {PM25_counter} Count: {count}')


    if PM_25_calc(PM_25) < 0:
        PM_25_max = PM_25_calc(PM_25)

    else:
        print(f'\tPM-2.5 concentration of {truncate(PM_25)}' + f' is index level {PM_25_calc(PM_25)}') # PRINT 1 #
        PM_25_max = PM_25_calc(PM_25)





    ### INPUT FOR CONCENTRATION OF PM10 ###
    PM_10 = math.floor(float(input(' -> Enter PM-10 concentration: '))) # INPUT 5 #
    if PM_10_calc(PM_10) < 0:
        PM_10_max = PM_10_calc(PM_10)
    else:
        print(f'\tPM-10 concentration of {PM_10} is index level {PM_10_calc(PM_10)}') # PRINT 2 #
        PM_10_max = PM_10_calc(PM_10)



    ### INPUT FOR CONCENTRATION OF NO_2 ###
    NO_2 = math.floor(float(input(' -> Enter NO-2 concentration: '))) # INPUT 6 #
    if NO_2_calc(NO_2) < 0:
        NO_2_max = NO_2_calc(NO_2)
    else:
        print(f'\tNO-2 concentration of {NO_2} is index level {NO_2_calc(NO_2)}') # PRINT 3 #
        NO_2_max = NO_2_calc(NO_2)



    ### INPUT FOR CONCENTRATION OF SO ###
    SO = math.floor(float(input(' -> Enter SO-2 concentration: '))) # INPUT 7 #
    if SO_calc(SO) < 0:
        SO_2_max = SO_calc(SO)
    else:
        print(f'\tSO-2 concentration of {SO} is index level {SO_calc(SO)}') # PRINT 4 #
        SO_2_max = SO_calc(SO)



    ### INPUT FOR CONCENTRATION OF CO ###
    CO = float(input(' -> Enter CO concentration: ')) # INPUT 8 #
    if CO_calc(CO) < 0:
        CO_max = CO_calc(CO)
    else:
        print(f'\tCO concentration of {truncate(CO)} is index level {CO_calc(CO)}') # PRINT 5 #
        CO_max = CO_calc(CO)



    ### INPUT FOR CONCENTRATION OF O_3 ###
    O_3 = math.floor(float(input(' -> Enter O3 concentration: '))) # INPUT 9 #
    if O_3_calc(O_3) < 125:
        O_3_max = O_3_calc(O_3)

    else:
        print(f'\tO3 concentration of {O_3} is index level {O_3_calc(O_3)}') # PRINT 6 #
        O_3_max = O_3_calc(O_3)


    ### PRINTS THE AQUI FOR A LOCATION AND GIVES THE AIR QUALITY FOR SAID LOCATION ###
    print(f'\nAQI for {name} is {Max(PM_25_max , PM_10_max, NO_2_max , SO_2_max , CO_max , O_3_max)}') # PRINT 7 #
    print(f"Air Quality: {quality}\n") # PRINT 8 #


    ### LIST TO HELP SOLVE FOR THE OVERALL SUMMARY OF THE LOCATIONS ###
    name_list.append(name)

    max_value.append(Max(PM_25_max , PM_10_max, NO_2_max , SO_2_max , CO_max , O_3_max))


### SOLVES FOR THE MAX VALUE BETWEEN ALL LOCATIONS ###
for j in max_value:
    if j > max:
        max = j


PM25_avg = PM25_counter / (count)


if PM25_avg < 0:
    print(f'Summary:\n\tLocation with the highest AQI is {name} ({max})') # PRINT 9 #

else:
    print(f'Summary:\n\tLocation with the highest AQI is {name} ({max})' + f'\nAverage PM-2.5 concentration: {truncate(PM25_avg)}') # PRINT 10 #