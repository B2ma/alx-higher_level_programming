#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc
    a = 10
    b = 5
    print("{} + {} = {}".format(int(a), int(b), int(calc.add(a, b))))
    print("{} - {} = {}".format(int(a), int(b), int(calc.sub(a, b))))
    print("{} * {} = {}".format(int(a), int(b), int(calc.mul(a, b))))
    print("{} / {} = {}".format(int(a), int(b), int(calc.div(a, b))))
