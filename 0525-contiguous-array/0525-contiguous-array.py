class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        store = {}
        count = 0
        longest = 0
        for i, num in enumerate(nums):
            count += num if num == 1 else -1
            
            if count == 0:
                longest = max(longest, i+1)
                
            if count in store:
                longest = max(longest, i-store[count])
                        
            
            if count not in store:
                store[count] = i
        return longest