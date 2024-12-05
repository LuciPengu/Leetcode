class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxi = 0
        results = []
        n = len(s)
        for i in range(len(s)-1):
            
            if s[i] == s[i+1]:
                start = s[i] + s[i+1]
                l, r = i-1, i+2
                results.append(start)
                while l >= 0 and r < n and s[l] == s[r]:
                    start = s[l] + start + s[r]
                    results.append(start)
                    l -= 1
                    r += 1
                    
            start = s[i]
            l, r = i-1, i+1
            results.append(start)
            while l >= 0 and r < n and s[l] == s[r]:
                start = s[l] + start + s[r]
                results.append(start)
                l -= 1
                r += 1
        
        results.sort(key = lambda x:len(x))
        return results[-1] if n > 1 else s
            
                
                