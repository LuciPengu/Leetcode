class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1],[1,1]]
        start = 1
        for i in range(numRows):
            ans = list(res[-1])
            new = []
            for i in range(len(ans)-1):
                new.append(ans[i] + ans[i+1])
            
            res.append([1] + new + [1])
        return res[0:numRows]