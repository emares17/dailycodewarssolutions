# LeetCode 67. Add Binary

# Given two binary strings a and b, return their sum as a binary string.

 

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"

# ------------------------------Solution----------------------------------

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        carry = 0
        
        a = list(map(int,a))
        b = list(map(int,b))
                 
        while len(a) < len(b):
            a.insert(0,0)
        while len(b) < len(a):
            b.insert(0,0)
                 
        for i in range(len(a) - 1, -1, -1):
            current = a[i] + b[i] + carry
            res.insert(0, str(current % 2))
            carry = current // 2
                 
        if carry:
            res.insert(0, str(carry))
        
        return ''.join(res)