class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        
        cnt = 0
        k = 1
        maxi = -1
        for num in nums:
            if k >= 3 and cnt > num:
                maxi = max(maxi, cnt+num)
                
            cnt += num
            k += 1
        return maxi