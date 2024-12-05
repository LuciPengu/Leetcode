class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr = []
        
        maxi = 0
        currentS = 0
        for i in range(len(s)):
            curr = set()
            currentS = 0
            for j in range(i, len(s)):
                if s[j] in curr:
                    maxi = max(maxi, currentS)
                    break
                curr.add(s[j])
                currentS += 1
            maxi = max(maxi, currentS)
        return maxi