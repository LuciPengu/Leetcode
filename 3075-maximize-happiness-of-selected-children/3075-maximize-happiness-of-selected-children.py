class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        
        curr = 0
        res = 0
        for i in range(k):
            res += max(0,happiness.pop() - curr)            
            curr+=1

        return res