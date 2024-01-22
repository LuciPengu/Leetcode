class Solution:
    def rob(self, a: List[int]) -> int:
        def solve(ind,a):
            if ind==0:
                return a[ind]
            if ind<0:
                return 0
            if dp[ind]!=-1:
                return dp[ind]
            pick=a[ind]+solve(ind-2,a)
            non_pick=0+solve(ind-1,a)
            dp[ind]=max(pick,non_pick)
            return dp[ind]
        n=len(a)
        dp=[-1]*n
        return solve(n-1,a)