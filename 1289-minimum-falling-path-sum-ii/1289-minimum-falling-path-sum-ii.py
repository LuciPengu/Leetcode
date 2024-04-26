class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        found = set()
        @cache
        def dfs(x,y):

            if x == width-1:
                return grid[x][y]
            
            

            res = float("inf")
            for nextX in range(width):
                if nextX != y:
                    res = min(res, dfs(x+1, nextX))

            return res + grid[x][y]
        
        res = float("inf")
        for col in range(width):
            res = min(res, dfs(0,col))
        print(found)
        return min(res, dfs(0,0))
