class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        def validStr(string):
            return len(set(string)) == len(string)
        
        @cache
        def dfs(c,i):
            if i >= len(arr):
                return len(c)
            
            res = 0
            res = max(res,dfs(c,i+1))
            
            if validStr(c+arr[i]):
                res = max(res, dfs(c+arr[i],i+1))
            
            return res
                
        return dfs("",0)