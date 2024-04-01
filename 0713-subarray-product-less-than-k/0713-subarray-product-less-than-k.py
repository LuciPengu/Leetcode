class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count = 0
        l = 0
        curr = 1
        if k <= 1:
            return 0
        for r in range(len(nums)):
            curr *= nums[r]
            while(curr >= k):
                try:
                    curr /= nums[l]
                    l+=1
                except:
                    return count
                
            count += (r - l) + 1
        
        return count