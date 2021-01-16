from isOdd import isOdd
from isZero import isZero
import sys

# Simple program to determine if a number is even, odd, or zero.
# Built to be silly.

if __name__ == "__main__":
    number = int(input("Enter a number > "))
    if not isOdd(number):
        if not isZero(number):
            print(number, "is even.")
        else:
            print(number, "is zero.")
    else:
        print(number, "is odd.")

    