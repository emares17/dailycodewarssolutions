# LeetCode 2016. Maximum Difference Between Increasing Elements

# Given a 0-indexed integer array nums of size n, find the maximum difference between nums[i] and nums[j] 
# (i.e., nums[j] - nums[i]), such that 0 <= i < j < n and nums[i] < nums[j].

# Return the maximum difference. If no such i and j exists, return -1.

 

# Example 1:

# Input: nums = [7,1,5,4]
# Output: 4
# Explanation:
# The maximum difference occurs with i = 1 and j = 2, nums[j] - nums[i] = 5 - 1 = 4.
# Note that with i = 1 and j = 0, the difference nums[j] - nums[i] = 7 - 1 = 6, but i > j, so it is not valid.
# Example 2:

# Input: nums = [9,4,3,2]
# Output: -1
# Explanation:
# There is no i and j such that i < j and nums[i] < nums[j].
# Example 3:

# Input: nums = [1,5,2,10]
# Output: 9
# Explanation:
# The maximum difference occurs with i = 0 and j = 3, nums[j] - nums[i] = 10 - 1 = 9.

# ---------------------------------Solution-----------------------------------

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_diff = 0
        current_diff = 0
        minimum = nums[0]
        
        for num in nums:
            if num < minimum:
                minimum = num
            else:
                current_diff = num - minimum
                max_diff = max(max_diff, current_diff)
        
        return max_diff if max_diff > 0 else -1