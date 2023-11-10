# LeetCode 169. Majority Element

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

# ----------------------Solution-------------------------

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = len(nums) / 2
        nums_dict = {}
        for num in nums:
            nums_dict[num] = nums_dict.get(num, 0) + 1
            
        for key, val in nums_dict.items():
            if val > majority:
                return key
            