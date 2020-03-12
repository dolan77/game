user_input = input()

character = user_input[0:1]

word_choice = user_input[2:]

count = 0

for i in word_choice:
    if i == character:
        count += 1

print(count)