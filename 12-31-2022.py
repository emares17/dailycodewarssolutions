# Simple multiplication

# This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.

# -----------------------------------Solution----------------------------------

def simple_multiplication(number) :
    return number * 8 if number % 2 == 0 else number * 9