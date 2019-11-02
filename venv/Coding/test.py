for num in range(0, 20, 5):
    num += num
print(str(num) + '\n')

total = 0
for count in range(4,6):
    total += count
    print(total)

print('\n')

total = 0
for count in range(1,4):
    total += count
print(total)

def main():
    first_name = input('Enter your first name:')
    last_name = input('Enter your last name: ')
    print('{} {}'.format(first_name, last_name))
    show(first_name,last_name)

def show(invert_first, invert_last):
    print('Time to invert your name')
    print('{} {}'.format(invert_last,invert_first))
    print(invert_last + ' ' +  invert_first)

main()
x = 2
number = 0
def reee():
    global number, x

    x = 4
    number = 9
    print(x)
    print(number)

reee()