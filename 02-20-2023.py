# LeetCode 709. To Lower Case

# Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

 

# Example 1:

# Input: s = "Hello"
# Output: "hello"
# Example 2:

# Input: s = "here"
# Output: "here"
# Example 3:

# Input: s = "LOVELY"
# Output: "lovely"

# ---------------------------Solution-------------------------------

class Solution:
    def toLowerCase(self, s: str) -> str:
        res = ''
        for i in s:
            if i.upper():
                res += i.lower()
            else:
                res += i
        return res