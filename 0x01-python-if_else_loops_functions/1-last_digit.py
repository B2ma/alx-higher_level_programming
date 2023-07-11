#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
statement1 = f"Last digit of {number} is "
statement2 = f"{-int(str(number)[-1]) if number < 0 else int(str(number)[-1])}"
if int(str(number)[-1]) > 5 and number > 0:
    print(f"{statement1}{statement2 } and is greater than 5")
elif int(str(number)[-1]) == 0:
    print(f"{statement1}{statement2 } and is 0")
elif int(str(number)[-1]) < 6 and int(str(number)[-1]) != 0 and number > 0:
    print(f"{statement1}{statement2 } and is less than 6 and not 0")
elif int(str(number)[-1]) > 6 and int(str(number)[-1]) != 0 and number < 0:
    print(f"{statement1}{statement2 } and is less than 6 and not 0")
elif int(str(number)[-1]) < 6 and int(str(number)[-1]) != 0 and number < 0:
    print(f"{statement1}{statement2 } and is less than 6 and not 0")
