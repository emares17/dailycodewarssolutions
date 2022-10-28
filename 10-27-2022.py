# Make the Deadfish Swim

# Write a simple parser that will parse and run Deadfish.

# Deadfish has 4 commands, each 1 character long:

# i increments the value (initially 0)
# d decrements the value
# s squares the value
# o outputs the value into the return array
# Invalid characters should be ignored.

# parse("iiisdoso")  ==>  [8, 64]

# ------------------------------Solution------------------------------

def parse(data):
    stack = []
    count = 0
    data = list(data)
    for i in data:
        if i == 'i': count += 1
        elif i == 'd': count -= 1
        elif i == 's': count = count ** 2
        elif i == 'o': stack.append(count)
    return stack