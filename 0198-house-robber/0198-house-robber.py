class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        @cache
        def getRobbed(ptr):
            if ptr >= len(nums):
                return 0
            return nums[ptr] + max(getRobbed(ptr+2), getRobbed(ptr+3))

        return getRobbed(-2) - nums[-2]