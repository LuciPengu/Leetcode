class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjlist = defaultdict(list)
        for start, end in edges:
            adjlist[start].append(end)
            adjlist[end].append(start)
        
        visited = set()
        def dfs(i):
            if i == destination:
                return True
            if i in visited:
                return False
            visited.add(i)
            res = False
            for j in adjlist[i]:
                if dfs(j):
                    res = True
            
            return res
        return dfs(source)