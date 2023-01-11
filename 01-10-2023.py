# Permute a Palindrome

# Write a function that will check whether ANY permutation of the characters of the input string is a palindrome. 
# Bonus points for a solution that is efficient and/or that uses only built-in language functions. Deem yourself brilliant 
# if you can come up with a version that does not use any function whatsoever.

# Example
# madam -> True
# adamm -> True
# junk -> False

# Hint
# The brute force approach would be to generate all the permutations of the string and check each one of them 
# whether it is a palindrome. However, an optimized approach will not require this at all.

# ---------------------------Solution-----------------------------

def permute_a_palindrome (input):
    count = {}
    for i in input:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    odd_count = 0
    for key in count:
        if count[key] % 2 != 0:
            odd_count += 1
    return odd_count <= 1