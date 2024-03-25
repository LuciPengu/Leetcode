class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        res = []
        for i in count:
            if count[i] == 2:
                res.append(i)
        return res