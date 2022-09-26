# Snail

# Snail Sort
# Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]
# For better understanding, please follow the numbers of the next array consecutively:

# array = [[1,2,3],
#          [8,9,4],
#          [7,6,5]]
# snail(array) #=> [1,2,3,4,5,6,7,8,9]
# This image will illustrate things more clearly:


# NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array 
# in a clockwise snailshell pattern.

# NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].

# -------------------------------Solution---------------------------------

def snail(snail_map):
    stack = []
    
    while snail_map:
        for i in snail_map[0]:
            stack.append(i)
        snail_map.pop(0)
        
        if not snail_map:
            break
        
        for j in snail_map:
            stack.append(j[-1])
            j.pop()
        
        for k in range(len(snail_map[-1]) -1, -1, -1):
            stack.append(snail_map[-1][k])
        snail_map.pop()
        
        if not snail_map:
            break
        
        for l in reversed(snail_map):
            stack.append((l[0]))
            l.pop(0)
    return stack