# LeetCode 387. First Unique Character in a String

# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

# Example 1:

# Input: s = "leetcode"
# Output: 0
# Example 2:

# Input: s = "loveleetcode"
# Output: 2
# Example 3:

# Input: s = "aabb"
# Output: -1
 
# ------------------------------Solution----------------------------------

class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}
        for char in s:
            hashmap[char] = hashmap.get(char, 0) + 1
        for index, value in enumerate(s):
            if value in hashmap and hashmap[value] == 1:
                return index
        return -1