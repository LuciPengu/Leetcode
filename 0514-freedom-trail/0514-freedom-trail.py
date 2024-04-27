class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        def length(i, char):
            
            j = i
            length = 1
            while ring[j] != char:
                j += 1
                length += 1
                if j >= len(ring):
                    j = 0
            rightstore = [j, length]
            
            j = i
            length = 1
            while ring[j] != char:
                j -= 1
                length += 1
            
            leftstore = [j if j >= 0 else len(ring)+j, length]
            return [rightstore, leftstore]
        
        @cache
        def dfs(curr, i):
            
            if i == len(key):
                return 0
            
            right, left = length(curr, key[i])
            
            res = float("inf")
            print(right, left)
            res = min(res, dfs(right[0],i+1) + right[1])
            res = min(res, dfs(left[0],i+1) + left[1])
            return res
        
        return dfs(0,0)