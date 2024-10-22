# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        stack = [root]
        levels = []
        while stack:
            
            temp = []
            total = 0
            
            for node in stack:
                total += node.val
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            
            levels.append(total)
            stack = temp
        levels.sort(reverse=True)
        print(levels)

        if len(levels) < k:
            return -1
        
        return levels[k-1]
            