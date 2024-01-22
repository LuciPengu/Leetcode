class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dfs(i,c):
            if i >= len(nums):
                return c  
            return max(dfs(i+1,c),dfs(i+2,c+nums[i]))
        return dfs(0,0)
            