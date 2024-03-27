class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        @cache
        def dfs(i,count):
            if count >= k:
                return 0
            
            if i >= n:
                
                return 1 if count > 0 else 0
            
            res = 0
            
            res += dfs(i+1, nums[i] if count == 0 else count*nums[i])
            res += dfs(n, count)
            
            return res
        
        count = 0
        for i in range(n):
            count += dfs(i,0)
            
        return count