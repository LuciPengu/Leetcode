class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        adjlist = defaultdict(list)
        inpath = defaultdict(int)
        outpath = defaultdict(int)
        
        for start, end in pairs:
            adjlist[start].append(end)
            inpath[start] += 1
            outpath[end] += 1
        
        startnode = pairs[0][0]
        for curr in inpath:
            if inpath[curr] - outpath[curr] == 1:
                startnode = curr
        
        path = []
        visited = set()
        def dfs(node):
            while adjlist[node]:
                next_node = adjlist[node].pop()
                dfs(next_node)
            path.append(node)
            
        dfs(startnode)
        print(path)
        
        return [[path[i+1], path[i]] for i in reversed(range(len(path) - 1))]
            
            