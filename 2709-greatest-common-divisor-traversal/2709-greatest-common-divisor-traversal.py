class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        dicto = {}
        def prime_factors(n):
            i = 2
            factors = set()
            while i * i <= n:
                if n % i:
                    i += 1
                else:
                    n //= i
                    factors.add(i)
            if n > 1:
                factors.add(n)
            return factors
        
        seen = {}
        adjlist = defaultdict(list)
        for i in range(len(nums)):
            for prime in prime_factors(nums[i]):
                if prime in seen:
                    adjlist[i].append(seen[prime])
                    adjlist[seen[prime]].append(i)
                else:
                    seen[prime] = i
                        
        visited = set()
        def dfs(i):
            if i in visited:
                return
            visited.add(i)
            for j in adjlist[i]:
                dfs(j)
                
        dfs(0)
        
        return len(visited) == len(nums)