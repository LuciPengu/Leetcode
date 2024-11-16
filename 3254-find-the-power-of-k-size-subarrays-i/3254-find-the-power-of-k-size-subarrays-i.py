from sortedcontainers import SortedList
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        
        
        if k == 1:
            return nums
        n = len(nums)
        count = 0
        ans = []
        prev = -1
        for i in range(k):
            if nums[i] == prev + 1 or prev == -1:
                count += 1
            else:
                count = 1
            prev = nums[i]
        if count == k:
            ans.append(nums[i])
        else:
            ans.append(-1)
        print(ans, prev, count)
        
        for i in range(k, n):
            print(nums[i])
            if nums[i] == prev + 1:
                if count+1 >= k:
                    ans.append(nums[i])
                else:
                    ans.append(-1)
                    count += 1
            
            else:
                ans.append(-1)
                count = 1
            
            prev = nums[i]
        return ans
        