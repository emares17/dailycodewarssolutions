# LeetCode 1004. Max Consecutive Ones III

# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

# Example 1:

# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
# Example 2:

# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

# -----------------------------Solution-------------------------------

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l,ans = 0, 0
        counts = {0: 0, 1: 0}
        
        for idx, v in enumerate(nums):
            counts[v] += 1
            
            while counts[0] > k:
                counts[nums[l]] -= 1
                l += 1
                
            window = idx - l + 1
            ans = max(ans, window)
            
        return ans