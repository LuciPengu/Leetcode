class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        
        n = len(nums)
        
        def primeFactors(n):
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
        for i in range(n):
            for prime in primeFactors(nums[i]):
                if prime in seen:
                    adjlist[i].append(seen[prime])
                    adjlist[seen[prime]].append(i)
                else:
                    seen[prime] = i
        
        print(adjlist)
        visited = set()
        def dfs(i):
            if i in visited:
                return
            visited.add(i)
            for j in adjlist[i]:
                dfs(j)
                
        dfs(0)
        
        return len(visited) == n