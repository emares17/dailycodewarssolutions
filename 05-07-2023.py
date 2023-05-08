# LeetCode 



# ------------------------------Solution---------------------------------

class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        stack = []
        nums.sort()
        while sum(nums) > sum(stack):
            stack.append(nums.pop())
        if sum(nums) == sum(stack):
            stack.append(nums.pop())
        return stack