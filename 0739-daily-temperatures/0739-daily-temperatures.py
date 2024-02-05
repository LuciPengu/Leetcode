class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        soln = [0] * len(temp)
        stack = []
        for i, t in enumerate(temp):
            while(stack and stack[-1][0] < t):
                te, ind = stack.pop()
                soln[ind] = i - ind
            stack.append([t,i])
        return soln