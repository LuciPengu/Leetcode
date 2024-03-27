class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        nums = list(filter(lambda x: x>0, set(nums)))
        if nums == []:
            return 1
        nums.sort()
        
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        return i+2