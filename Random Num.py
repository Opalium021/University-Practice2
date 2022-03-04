#Python
#Javad Razaz Rahmaty
#Random Unique Num

import random

num = []

n = 0

i = 0

while True:

    get_num = input("Enter Length = ")

    if get_num.isdigit() and int(get_num) > 0:

        n = int(get_num)
        break

    else:
        print("\n\nPlease Enter a Valid Number")


    while i < n:
        x = random.choice(range(1000))

        if x not in num:

            num.append(x)

            i += 1 
