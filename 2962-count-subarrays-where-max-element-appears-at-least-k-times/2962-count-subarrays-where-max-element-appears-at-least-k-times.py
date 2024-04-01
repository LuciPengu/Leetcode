class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        elemfreq = 0
        maxelem = max(nums)
        
        res = l = 0
        
        for r in range(len(nums)):
            if nums[r] == maxelem:
                elemfreq += 1
            
            
            while elemfreq == k:
                
                if nums[l] == maxelem:
                    elemfreq -= 1
                    
                l += 1
            
            res += l
        return res