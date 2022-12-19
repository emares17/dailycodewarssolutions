# Double Every Other

# Write a function that doubles every second integer in a list, starting from the left.

# Example:

# For input array/list :

# [1,2,3,4]
# the function should return :

# [1,4,3,8]

# -------------------------Solution---------------------------

def double_every_other(list):
    return [v * 2 if not i % 2 else v for i, v in enumerate(list, 1)]