class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = Counter(nums)
        seen = set()
        res = 0
        for i in count:
            if i in seen:
                continue
            while(count[i]) >= 5:
                count[i] -= 3
                res += 1
            if count[i] % 3 == 0:
                res += count[i]//3
            elif count[i] % 2 == 0:
                res += count[i]//2
                seen.add(i)
            else:
                return -1
        return res