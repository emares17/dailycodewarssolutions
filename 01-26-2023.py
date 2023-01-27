# LeetCode 14. Longest Common Prefix

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# ---------------------------Solution-----------------------------

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = ''
        prefix = strs[0]
        for string in strs[1:]:
            while string[:len(prefix)] != prefix and prefix:
                prefix = prefix[:len(prefix) - 1]
            if not prefix:
                break
        longest = prefix
        return longest