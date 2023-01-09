# Micro Optimization: Digit Sum

# You wrote a program that can calculate the sum of all the digits of a non-negative integer.

# However, it's not fast enough. Can you make it faster?

# ----------------------------Solution--------------------------------

def digit_sum(n):
    return sum([int(i) for i in str(abs(n))])