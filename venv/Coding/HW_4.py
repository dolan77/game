# declaring variables

route_number = 1

while route_number != 0 and route_number > 0:

    route_number = int(input('Please enter a US Interstate Highway route number: '))

    # checks to see if input of route_number is 0 and breaks the loop

    if route_number == 0:
        break

    # input validation to make sure route_number is between 0 and 999.

    while route_number < 0 or route_number > 999:
        route_number = int(input('Please enter a US Interstate Highway route number: '))

    # if statement that checks if route_number is a primary route

    if route_number < 100:

        # if statement that checks if the route_number is even, else it is odd. Will give the
        # route_orientation based on whether it is even or odd

        if route_number % 2 == 0:

            route_orientation = 'east-west'

        else:
            route_orientation = 'north-south'

        # determines of route_number is a multiple of 5, if so, makes route_size a long-diistance arterial

        if route_number % 5 == 0:
            route_size = True

        else:
            route_size = False

    # else loop that is for a 3 digit number, an auxiliary route

    else:

        # will convert route_number to a string in order to cut the last two digits off
        # works only for auxiliary highways

        string_number = str(route_number)

        last_two_digits = string_number[1:]

        # a little while loop to grab the first digit of the three digit route_number

        first_digit = route_number

        while first_digit >= 10:
            first_digit = first_digit // 10

        # checks to see if the first digit of route_number is even, if so, the route is a loop highway

        if first_digit % 2 == 0:

            route_type = 'loop'

        else:

            route_type = 'spur'

    # if statement that prints the primary route

    if route_number < 100:

        if route_size == True:

            print(f'Interstate {route_number} is a long-distance arterial highway oriented {route_orientation}.')

        else:
            print(f'Interstate {route_number} is oriented {route_orientation}.')

    # else statement that prints the auxiliary route

    else:
        print(f'Interstate {route_number} is a {route_type} highway of Interstate {int(last_two_digits)}.')
