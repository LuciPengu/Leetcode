class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        ans = list(filter(lambda x: x>0, set(nums)))
        if ans == []:
            return 1
        ans.sort()
        
        for i in range(len(ans)):
            if ans[i] != i+1:
                return i+1
        return i+2