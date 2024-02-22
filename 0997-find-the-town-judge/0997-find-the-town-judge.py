class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted = defaultdict(int)
        trusts = defaultdict(int)
        for t1, t2 in trust:
            trusted[t2]+=1
            trusts[t1]+=1
        
        print(trusted,trusts)
        for i in range(1,n+1):
            print(i)
            if trusted[i] == n-1 and trusts[i] == 0:
                return i
        return -1