# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root, path):
            
            if root == None:
                return 0
            curr = str(root.val)
            if root.left == None and root.right == None:
                return int(path+curr)
            return dfs(root.left, path+curr) + dfs(root.right, path+curr)
      
        return dfs(root, "")
