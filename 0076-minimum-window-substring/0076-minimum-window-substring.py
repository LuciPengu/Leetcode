class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, r = 0, 0
        n = len(s)
        tcount = Counter(t)
        count = Counter(defaultdict(int))
        
        def check(tcount, count):
            #print(tcount - count)
            return tcount - count == Counter()
        
        maxi = float("inf")
        res = ""
        while True:
            #print(s[l:r], count)

            if check(tcount, count):
                if maxi > r-l:
                    maxi = r-l
                    res = s[l:r]
                    
                count[s[l]] -= 1
                l += 1
            
            elif r < n:
                count[s[r]] += 1
                r += 1
            
            else:
                break
        return res