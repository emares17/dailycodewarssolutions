# LeetCode 2441. Largest Positive Integer That Exists With Its Negative

# Given an integer array nums that does not contain any zeros, find the largest positive integer 
# k such that -k also exists in the array.

# Return the positive integer k. If there is no such integer, return -1.

 

# Example 1:

# Input: nums = [-1,2,-3,3]
# Output: 3
# Explanation: 3 is the only valid k we can find in the array.
# Example 2:

# Input: nums = [-1,10,6,7,-7,1]
# Output: 7
# Explanation: Both 1 and 7 have their corresponding negative values in the array. 7 has a larger value.
# Example 3:

# Input: nums = [-10,8,6,7,-2,-3]
# Output: -1
# Explanation: There is no a single valid k, we return -1.

# -------------------------Solution--------------------------

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        stack = []
        for a in range(len(nums)):
            for b in range(a + 1, len(nums)):
                if abs(nums[a]) == abs(nums[b]) and nums[a] + nums[b] == 0:
                    stack.append((nums[a],nums[b]))
        
        if len(stack) > 0:
            max_tuple = max(stack, key=lambda x: abs(x[0]))
            return max(abs(max_tuple[0]), abs(max_tuple[1]))
        else:
            return -1