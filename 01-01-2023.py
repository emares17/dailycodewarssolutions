# Sum of prime-indexed elements

# In this Kata, you will be given an integer array and your task is to return the sum of elements occupying prime-numbered indices.

# The first element of the array is at index 0.

# Good luck!

# -----------------------------------Solution--------------------------------------

def prime_number(number):
    for i in range(2, number):
        if (number % i) == 0:
            return False    
    else:
        return True       

def total(arr):
    stack = []
    for i, v in enumerate(arr):
        if i >= 2 and prime_number(i):
            stack.append(v)
    return sum(stack)