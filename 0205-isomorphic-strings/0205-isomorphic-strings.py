class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        dicto = defaultdict(str)
        
        dicto2 = defaultdict(str)
        
        for i in range(len(s)):
            
            
            if (dicto[s[i]] and dicto[s[i]] != t[i]) or (dicto2[t[i]] and dicto2[t[i]] != s[i]):
                return False
            
            dicto[s[i]] = t[i]
            dicto2[t[i]] = s[i]
            
            
            
        return True