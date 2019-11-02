work_hrs = int(input("Enter the amount of hours you worked: "))

rate = 12

new_rate = 18

if work_hrs > 20:
    extra_hrs = work_hrs-20
    max_hrs = 20
    print("Your pay is: $" + str(rate*max_hrs + extra_hrs*new_rate))

elif work_hrs >= 0 & work_hrs <= 20:
    print("Your pay is: $" + str(rate*work_hrs))

else:
    print("Sorry, I didn't understand that")