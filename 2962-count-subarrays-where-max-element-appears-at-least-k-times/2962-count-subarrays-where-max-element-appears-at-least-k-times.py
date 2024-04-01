class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxelem = max(nums)
        elemCount = 0
        l = 0
        res = 0
        for r in range(len(nums)):
            if nums[r] == maxelem:
                elemCount += 1
            while elemCount >= k:
                if nums[l] == maxelem:
                    elemCount -= 1
                l += 1
            
            res += l
        return res
            
            