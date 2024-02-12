class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return max(((set(nums))), key = lambda x:nums.count(x))