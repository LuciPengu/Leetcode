class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 26
        
        for i in range(len(s)):
            curr = ord(s[i]) - ord('a')
            biggest = 1
            for nex in range(26):
                if abs(curr-nex) <= k:
                    biggest = max(biggest, dp[nex]+1)
            
            dp[curr] = max(biggest, dp[curr])
        print(dp)
        return max(dp)