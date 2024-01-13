class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        count1 = 0
        count2 = 0
        v = ["a","e","i","o","u"]
        for i in range(0,len(s)//2):
            if s[i].lower() in v:
                count1 += 1
        for i in range(len(s)//2,len(s)):
            if s[i].lower() in v:
                count2 += 1
        return count1 == count2