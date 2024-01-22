class Solution(object):
    def rob(self, nums):
        dp = [0] * len(nums)
        if len(nums) <= 2:
            return max(nums)
        for i in range(len(nums)):
            dp[i] = max(nums[i]+dp[i-2], dp[i-1])
        print(dp) 
        return max(dp)