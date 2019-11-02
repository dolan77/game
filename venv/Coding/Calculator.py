
while True:
    question = input('Would you like to add numbers? y/n ')

    if question.lower() == 'y':
        numbers_list = []

        numbers_list.append(int(input('Plese add the numbers you would like to add ')))

        print(numbers_list)
    else:
        exit()


