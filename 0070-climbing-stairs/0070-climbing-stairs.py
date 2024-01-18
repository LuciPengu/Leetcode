class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def dfs(i):
            if i == n:
                return 1
            if i >= n:
                return 0
            res = 0
            res += dfs(i+1)
            res += dfs(i+2)
            
            return res
        return dfs(0)