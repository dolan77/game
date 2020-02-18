import math

c = 299_792_458

value = float(input('Enter the velocity of the space ship as a fraction of the speed of light: '))

velocity = value * c

dialation = math.sqrt(1 - ( (velocity**2)) / (c**2) )

SECONDS_PER_DAY = 86400


### DISTANCE FROM EARTH TO PROXIMA ALPHA ###
distance = 7.4740 * 10**16

### TIME IS IN SECONDS ###
time = distance / velocity

time_on_earth = int(time)

time_on_ship = int(dialation * time)

# print( 'THE SECONDS' ,time_on_earth , time_on_ship)


### YEARS AND DAYS ON EARTH
days = int(time_on_earth / SECONDS_PER_DAY)

years = int(days / 365)

extra_days = int(days % 365)

print('An observer on Earth ages {} years, {} days during the trip.'.format(years , extra_days))


### YEARS AND DAYS ON SHIP ###

ship_days = int(time_on_ship / SECONDS_PER_DAY)

ship_years = int(ship_days / 365)

ship_extra_days = int(ship_days % 365)

print('A passenger on the ship ages {} years, {} days during the trip.'.format(ship_years , ship_extra_days))