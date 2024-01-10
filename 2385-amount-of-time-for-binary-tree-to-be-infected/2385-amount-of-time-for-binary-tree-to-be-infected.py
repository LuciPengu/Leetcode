# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        adjlist = defaultdict(list)
        def dfs(node):
            if node == None:
                return
            if node.left:
                adjlist[node.val].append(node.left.val)
                adjlist[node.left.val].append(node.val)
                dfs(node.left)
            if node.right:
                adjlist[node.val].append(node.right.val)
                adjlist[node.right.val].append(node.val)
                dfs(node.right)
        
        dfs(root)

        visited = set()
        maxi = 0
        def dfslist(i, p):
            nonlocal maxi
            if i in visited:
                return

            visited.add(i)
            maxi = max(maxi, p)
            for node in adjlist[i]:
                dfslist(node, p+1)
        
        dfslist(start,0)
        return maxi
            
            