class Solution:
    def countSubarrays(self, nums: List[int], mink: int, maxK: int) -> int:
        last = -1
        l, r = -1, -1
        res = 0
        for i in range(len(nums)):
            if not mink <= nums[i] <= maxK:
                last = i
            
            if nums[i] == mink:
                l = i
            
            if nums[i] == maxK:
                r = i
            
            print(l,r,last)
            res += max(0, min(l,r)-last)
        return res