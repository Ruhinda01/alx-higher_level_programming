#!/usr/bin/python3



def fizzbuzz():
    for c in range(1, 101):
        if c % 3 == 0 and c % 5 == 0:
            print("FizzBuzz", end=" ")
        elif c % 3 == 0:
            print("Fizz", end=" ")
        elif c % 5 == 0:
            if c == 100:
                print("Buzz", end="")
            else:
                print("Buzz", end=" ")
        else:
            print("{:d}".format(c), end=" ")
