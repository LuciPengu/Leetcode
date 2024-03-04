# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        prev = [root]
        tempqueue = [root]
        while queue:
            prev = tempqueue
            tempqueue = []
            for node in queue:
                if node.left:
                    tempqueue.append(node.left)
                if node.right:
                    tempqueue.append(node.right)
            queue = tempqueue
        print(tempqueue)
        return prev[0].val
        