#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
the_statement = f"Last digit of {number} is {-int(str(number)[-1]) if number < 0 else int(str(number)[-1])}"
if int(str(number)[-1]) > 5:
    print(f"{the_statement } and is greater than 5")
elif int(str(number)[-1]) == 0:
    print(f"{the_statement } and is 0")
elif int(str(number)[-1]) < 6 and int(str(number)[-1]) != 0:
    print(f"{the_statement } and is less than 6 and not 0")
