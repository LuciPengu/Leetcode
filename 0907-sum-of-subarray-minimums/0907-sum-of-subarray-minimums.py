class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        stack = []
        res = 0
        arr += [float("-inf")]
        for i, n in enumerate(arr):
            while stack and n < stack[-1][1]:
                j, m = stack.pop()
                
                left = j - stack[-1][0] if stack else j+1
                right = i - j
                
                res += m * left * right
            stack.append((i,n))
        
        return res %(10 ** 9 + 7)