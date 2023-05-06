# LeetCode 977. Squares of a Sorted Array

# Given an integer array nums sorted in non-decreasing order, return an array of the 
# squares of each number sorted in non-decreasing order.

 

# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# Example 2:

# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

# ---------------------------Solution-------------------------------

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        stack = [0] * len(nums)
        l,r = 0, len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if abs(nums[l]) > abs(nums[r]):
                stack[i] = nums[l] ** 2
                l += 1
            else:
                stack[i] = nums[r] ** 2
                r -= 1
        return stack