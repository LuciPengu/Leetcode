class Solution:
    def combinationSum2(self, c: List[int], target: int) -> List[List[int]]:
        c.sort()
        
        ans = set()
        @cache
        def dp(i, path):
            if sum(path) == target:
                ans.add(path)
                print("d",path)
            if sum(path) > target or i >= len(c):
                return
            
            dp(i+1,path)
            dp(i+1,path+tuple([c[i]]))
            
        dp(0,())
        return ans