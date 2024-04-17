# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        alpha = "abcdefghijklmnopqrstuvwxyz"
        res = []
        def dfs(root, path):
            if root == None:
                return
            if root.left == None and root.right == None:
                
                res.append((path+alpha[root.val])[::-1])
            
            dfs(root.left, path+ alpha[root.val])
            dfs(root.right, path + alpha[root.val])
        
        dfs(root, "")
        res.sort()
        
        print(res)
        return res[0]    
            