# Method to determine if a number is odd
def isOdd(n):
    n *= 3
    if (n / 3) % 2 != 0:
        return True
    return False