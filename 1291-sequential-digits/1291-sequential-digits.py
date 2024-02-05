class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        nums = "123456789"
        ans = []
        l = len(str(low))
        h = len(str(high))
        for size in range(l,h+1):
            for i in range(len(nums)-size+1):
                if size == h and int(nums[i:i+size]) > high:
                    break
                elif size == l and int(nums[i:i+size]) < low:
                    continue
                ans.append(int(nums[i:i+size]))
        print(ans)
        return ans