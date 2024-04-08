class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        size = len(profit)-1
        MOD = (10**9 + 7)
        @cache
        def dfs(i, money, men):
            
            
            if i > size:
                return 1 if money >= minProfit else 0
            
            
            res = 0
            if men >= group[i]:
                res += dfs(i+1, min(minProfit, money+profit[i]), men-group[i])
            
            res += dfs(i+1, money, men)
            
            return res
        
        return dfs(0,0,n) % MOD