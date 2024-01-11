# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        maxi = 0
        def dfs(node, maxan, minan):
            nonlocal maxi
            if node == None:
                return
            
            maxi = max(maxi, maxan-node.val, node.val-minan)
            dfs(node.left,max(maxan,node.val), min(minan, node.val))
            dfs(node.right,max(maxan,node.val), min(minan,node.val))
        
        dfs(root,0,float("inf"))
        return maxi