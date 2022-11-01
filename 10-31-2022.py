# Debug Sum of Digits of a Number

# Debug function getSumOfDigits that takes positive integer to calculate sum of it's digits. Assume that argument is an integer.

# Example
# 123  => 6
# 223  => 7
# 1337 => 14

# ----------------------------Solution-----------------------------

def get_sum_of_digits(num):
    sum = 0
    digits = list(map(int, str(num)))
    for x in digits:
        sum += x
    return sum