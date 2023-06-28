# 1446. Consecutive Characters

# The power of the string is the maximum length of a non-empty substring that contains only one 
# unique character.

# Given a string s, return the power of s.

 

# Example 1:

# Input: s = "leetcode"
# Output: 2
# Explanation: The substring "ee" is of length 2 with the character 'e' only.
# Example 2:

# Input: s = "abbcccddddeeeeedcba"
# Output: 5
# Explanation: The substring "eeeee" is of length 5 with the character 'e' only.

# ---------------------------Solution------------------------------

class Solution:
    def maxPower(self, s: str) -> int:
        l = 0
        count = 1
        for r in range(1, len(s)):
            if s[l] == s[r]:
                count = max(count, r - l + 1)
            else:
                l = r
        return count